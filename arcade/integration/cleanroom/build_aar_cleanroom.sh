#!/usr/bin/env bash
# Build the arcade embed for release, in the Linux clean-room container.
# (AUDIT-v1.0.8-2026-09-29.md, P1: an AAR built on Windows cannot be
# reproduced by the clean room, and the policy's ship gate refuses it.)
#
#   build_aar_cleanroom.sh <v1-tag-or-commit> [--publish]
#
# Run from Git Bash on the Windows machine. Steps:
#   1. bundle puzzle-app at that ref (it must be clean, and on main)
#   2. container from dgd-cleanroom-flutter:1, sources in by `docker cp`, no mounts
#   3. online: fetch packages under the v1 lockfile, build A
#   4. network cut: clean, build B offline, require A == B
#   5. copy B and PROVENANCE.md out; with --publish, mirror them into
#      dgd-native/android/arcade-repo
# The container is always deleted. build_aar.cmd still exists for quick local
# builds, but only this script's output is fit to ship.
set -euo pipefail
export MSYS_NO_PATHCONV=1
REF="${1:?usage: build_aar_cleanroom.sh <v1-tag-or-commit> [--publish]}"; PUBLISH="${2:-}"
HERE="$(cd "$(dirname "$0")" && pwd)"
V1=C:/src/puzzle-app
NATIVE_REPO=C:/src/dgd-native/android/arcade-repo
IMAGE=dgd-cleanroom-flutter:1
STAGE="$(cygpath -m "${TMP:-/tmp}")/dgd-aar-$(date +%Y%m%dT%H%M%S)"
C=dgd-aar-$$

[ -z "$(git -C $V1 status --porcelain)" ] || { echo "puzzle-app has uncommitted changes; commit first"; exit 1; }
COMMIT=$(git -C $V1 rev-parse "$REF^{commit}")
git -C $V1 merge-base --is-ancestor "$COMMIT" main || { echo "$REF is not on puzzle-app main"; exit 1; }
echo "v1 $REF = $COMMIT"

mkdir -p "$STAGE"
git -C $V1 bundle create "$STAGE/puzzle-app.bundle" main $(git -C $V1 tag --points-at "$COMMIT") > /dev/null 2>&1
IMAGE_ID=$(docker image inspect $IMAGE --format '{{.Id}}')

cleanup() { docker rm -f $C > /dev/null 2>&1 || true; }
trap cleanup EXIT
# 3.1 GB of RAM plus up to 1 GB of the VM's swap: a memory peak slows the
# build instead of the kernel killing Gradle mid-build.
docker create --name $C --memory 3100m --memory-swap 4100m -e DGD_IMAGE="$IMAGE $IMAGE_ID" \
  $IMAGE sleep infinity > /dev/null
[ "$(docker inspect $C --format '{{len .Mounts}}')" = 0 ] || { echo "container has mounts; refusing"; exit 1; }
docker start $C > /dev/null
docker exec $C mkdir -p /home/builder/in
for f in "$STAGE/puzzle-app.bundle" "$HERE/../sync_module.py" "$HERE/aar_in_container.sh"; do
  docker cp "$(cygpath -m "$f")" $C:/home/builder/in/ > /dev/null
done
docker exec -u 0 $C chown -R builder /home/builder/in

echo "== online: packages under the v1 lock, build A"
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
