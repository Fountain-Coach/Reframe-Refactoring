#!/usr/bin/env bash
# Publish the generated Reframe governance projection to its one authorized root.
#
# Tuple: governance.fountain.coach -> 65.109.14.71 -> /var/www/reframe-governance/current
# Dry-run is the default. Writing requires --apply --confirm-deploy. Promotion is staged and the
# previous current tree is retained under the exact deployment root's .rollback directory.

set -euo pipefail

HOST="governance.fountain.coach"
TARGET_IP="65.109.14.71"
REMOTE_BASE="/var/www/reframe-governance"
REMOTE_CURRENT="${REMOTE_BASE}/current"
REMOTE_RELEASES="${REMOTE_BASE}/.releases"
REMOTE_ROLLBACK="${REMOTE_BASE}/.rollback"

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
site_root="${repo_root}/site"
apply=0
confirm=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply) apply=1; shift ;;
    --confirm-deploy) confirm=1; shift ;;
    --help|-h)
      sed -n '2,9p' "$0"
      exit 0
      ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

[[ -d "$site_root" && -f "$site_root/index.html" ]] || {
  echo "refusing: generated site is missing: $site_root/index.html" >&2
  exit 2
}

if find "$site_root" -name '.DS_Store' -print -quit | grep -q .; then
  echo "refusing: generated site contains Finder metadata" >&2
  exit 2
fi

resolved="$(dig +short "$HOST" A 2>/dev/null | head -1)"
[[ "$resolved" == "$TARGET_IP" ]] || {
  echo "refusing: $HOST resolves to '${resolved:-nothing}', expected $TARGET_IP" >&2
  exit 3
}

ssh_user="${PUBLISHING_SSH_USER:-root}"
ssh_key="${PUBLISHING_SSH_KEY:-$HOME/.ssh/id_rsa}"
ssh_opts=(-o BatchMode=yes -o IdentitiesOnly=yes -o ConnectTimeout=10 -i "$ssh_key")
remote="${ssh_user}@${TARGET_IP}"

rsync_args=(-rlptv --checksum --delete
  --exclude '._*' --exclude '.DS_Store' --exclude '__pycache__/'
  -e "ssh ${ssh_opts[*]}")

echo "== governance deployment plan =="
echo "source: $site_root/"
echo "target: ${remote}:${REMOTE_CURRENT}/ (${HOST})"
echo "mode: $([[ $apply -eq 1 && $confirm -eq 1 ]] && echo APPLY || echo 'DRY RUN (pass --apply --confirm-deploy to write)')"

if [[ $apply -ne 1 || $confirm -ne 1 ]]; then
  rsync --dry-run "${rsync_args[@]}" "$site_root/" "${remote}:${REMOTE_CURRENT}/"
  echo "dry run only — nothing was written."
  exit 0
fi

stamp="$(date -u +%Y%m%dT%H%M%SZ)"
release="${REMOTE_RELEASES}/release-${stamp}-$$"
ssh "${ssh_opts[@]}" "$remote" "mkdir -p '$REMOTE_RELEASES' '$REMOTE_ROLLBACK' && test -d '$REMOTE_CURRENT'"
rsync "${rsync_args[@]}" "$site_root/" "${remote}:${release}/"
ssh "${ssh_opts[@]}" "$remote" \
  "chmod -R u=rwX,go=rX '$release' && mv '$REMOTE_CURRENT' '${REMOTE_ROLLBACK}/previous-${stamp}' && mv '$release' '$REMOTE_CURRENT'"

echo "== live verification =="
for route in "/" "/status-quo/" "/chapters/83-conversational-scenario-authoring/"; do
  code="$(curl -fsS -o /dev/null -w '%{http_code}' "https://${HOST}${route}")"
  [[ "$code" == 2* ]] || { echo "verification failed: $route -> $code" >&2; exit 4; }
  echo "${code} https://${HOST}${route}"
done
echo "published: ${remote}:${REMOTE_CURRENT}"
