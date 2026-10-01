#!/usr/bin/env bash
# Build the arcade embed for release, in the Linux clean-room container.
# (AUDIT-v1.0.8-2026-09-29.md, P1: an AAR built on Windows cannot be
# reproduced by the clean room, and the policy's ship gate refuses it.)
#
#   build_aar_cleanroom.sh <tag-or-commit> [--publish]
#   DGD_ARCADE=v2 build_aar_cleanroom.sh <v2-commit> [--publish]
#   DGD_ARCADE=v2 ARCADE_API=https://arcade.example build_aar_cleanroom.sh <v2-commit> [--publish]
#
# Without ARCADE_API the embed is the demo build (DGD_DEMO: no server, progress
# on the phone), which is what DGD App 2.0.0 ships. With it, the embed talks to
# that server instead. It must be a bare https URL: no trailing slash (the
# client appends /v1/...), no query, no credentials. PROVENANCE.md records the
# defines either way, and the native build prints them.
#
# DGD_ARCADE picks the arcade line, as in sync_module.py: v1 (the default,
# C:/src/puzzle-app on main) for DGD App 1.0.x, v2 (C:/src/puzzle-app-v2-wings
# on v2/ten-games) for DGD App 2.0.
#
# Run from Git Bash on the Windows machine. Steps:
#   1. bundle the arcade at that ref (it must be clean, and on its branch)
#   2. container from dgd-cleanroom-flutter:1, sources in by `docker cp`, no mounts
#   3. online: fetch packages under the arcade's lockfile, build A
#   4. network cut: clean, build B offline, require A == B
#   5. copy B and PROVENANCE.md out; with --publish, mirror them into
#      dgd-native/android/arcade-repo
# The container is always deleted. build_aar.cmd still exists for quick local
# builds, but only this script's output is fit to ship.
set -euo pipefail
export MSYS_NO_PATHCONV=1
REF="${1:?usage: [DGD_ARCADE=v2] build_aar_cleanroom.sh <tag-or-commit> [--publish]}"; PUBLISH="${2:-}"
HERE="$(cd "$(dirname "$0")" && pwd)"
ARCADE="${DGD_ARCADE:-v1}"
API="${ARCADE_API:-}"
if [ -n "$API" ]; then
  [[ "$API" =~ ^https://[A-Za-z0-9.-]+(:[0-9]{1,5})?(/[A-Za-z0-9._~-]+)*$ ]] || {
    echo "ARCADE_API=$API: it must be a bare https URL, with no trailing slash, query or credentials"; exit 1; }
  [ "$ARCADE" = v2 ] || { echo "ARCADE_API is for the v2 arcade; set DGD_ARCADE=v2"; exit 1; }
fi
case "$ARCADE" in
  v1) V1=C:/src/puzzle-app; BRANCH=main ;;
  v2) V1=C:/src/puzzle-app-v2-wings; BRANCH=v2/ten-games ;;
  *) echo "DGD_ARCADE=$ARCADE; it must be v1 or v2"; exit 1 ;;
esac
NATIVE_REPO=C:/src/dgd-native/android/arcade-repo
IMAGE=dgd-cleanroom-flutter:1
STAGE="$(cygpath -m "${TMP:-/tmp}")/dgd-aar-$(date +%Y%m%dT%H%M%S)"
C=dgd-aar-$$

[ -z "$(git -C $V1 status --porcelain)" ] || { echo "$V1 has uncommitted changes; commit first"; exit 1; }
COMMIT=$(git -C $V1 rev-parse "$REF^{commit}")
git -C $V1 merge-base --is-ancestor "$COMMIT" "$BRANCH" || { echo "$REF is not on $BRANCH in $V1"; exit 1; }
echo "$ARCADE $REF = $COMMIT"
if [ -n "$API" ]; then echo "embed config: ARCADE_API=$API"; else echo "embed config: demo (DGD_DEMO, no server)"; fi

mkdir -p "$STAGE"
git -C $V1 bundle create "$STAGE/puzzle-app.bundle" "$BRANCH" $(git -C $V1 tag --points-at "$COMMIT") > /dev/null 2>&1
IMAGE_ID=$(docker image inspect $IMAGE --format '{{.Id}}')

cleanup() { docker rm -f $C > /dev/null 2>&1 || true; }
trap cleanup EXIT
# 3.1 GB of RAM plus up to 1 GB of the VM's swap: a memory peak slows the
# build instead of the kernel killing Gradle mid-build.
docker create --name $C --memory 3100m --memory-swap 4100m -e DGD_IMAGE="$IMAGE $IMAGE_ID" -e DGD_ARCADE="$ARCADE" -e ARCADE_API="$API" \
  $IMAGE sleep infinity > /dev/null
[ "$(docker inspect $C --format '{{len .Mounts}}')" = 0 ] || { echo "container has mounts; refusing"; exit 1; }
docker start $C > /dev/null
docker exec $C mkdir -p /home/builder/in
for f in "$STAGE/puzzle-app.bundle" "$HERE/../sync_module.py" "$HERE/aar_in_container.sh"; do
  docker cp "$(cygpath -m "$f")" $C:/home/builder/in/ > /dev/null
done
docker exec -u 0 $C chown -R builder /home/builder/in

echo "== online: packages under the $ARCADE lock, build A"
docker exec $C bash /home/builder/in/aar_in_container.sh online "$COMMIT"

echo "== network cut"
for n in $(docker inspect $C --format '{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'); do
  docker network disconnect "$n" $C
done
docker exec $C bash -c 'getent hosts pub.dev >/dev/null 2>&1 && exit 1; exit 0' || { echo "network still up"; exit 1; }

echo "== offline: build B, compare with A"
OFFLINE=0
docker exec $C bash /home/builder/in/aar_in_container.sh offline "$COMMIT" || OFFLINE=$?

# Copy everything out before the container goes, pass or fail: a failed
# comparison is evidence too.
docker cp $C:/home/builder/out "$STAGE/out" > /dev/null
echo "staged in $STAGE"
[ "$OFFLINE" = 0 ] || { echo "offline build or comparison FAILED ($OFFLINE); nothing published"; exit 1; }
cp -r "$STAGE/out/B" "$STAGE/repo"
cp "$STAGE/out/PROVENANCE.md" "$STAGE/PROVENANCE.md"
grep -E "flutter_release-1.0.aar$" "$STAGE/PROVENANCE.md"

if [ "$PUBLISH" = "--publish" ]; then
  rm -rf "$NATIVE_REPO"
  cp -r "$STAGE/repo" "$NATIVE_REPO"
  cp "$STAGE/PROVENANCE.md" "$NATIVE_REPO/PROVENANCE.md"
  echo "published to $NATIVE_REPO"
fi
