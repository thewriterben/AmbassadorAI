#!/usr/bin/env bash
# Reproduce the DGD app's unsigned bundle in the clean-room container and
# compare it, entry by entry, with the one built on the host.
#
#   build_native_cleanroom.sh <dgd-native commit> <host-built .aab>
#
# Run from Git Bash on the Windows machine. The same method as the v1.0.8 pass
# (AUDIT-v1.0.8-2026-09-29.md): sources in as a git bundle by `docker cp`, no
# mounts; a warm build with the network on fills the Gradle cache; the network
# is cut, verified dead, and the evidence build runs offline; then the bundle
# comes out and is compared with the host's. The arcade AAR is whatever the
# commit holds in android/arcade-repo, so the app's own provenance gate runs
# inside the container too. The container is always deleted.
set -euo pipefail
export MSYS_NO_PATHCONV=1
REF="${1:?usage: build_native_cleanroom.sh <commit> <host .aab>}"; HOST_AAB="${2:?host .aab}"
HERE="$(cd "$(dirname "$0")" && pwd)"
NATIVE=C:/src/dgd-native
IMAGE=dgd-cleanroom:1
STAGE="$(cygpath -m "${TMP:-/tmp}")/dgd-native-$(date +%Y%m%dT%H%M%S)"
C=dgd-native-$$

COMMIT=$(git -C $NATIVE rev-parse "$REF^{commit}")
echo "dgd-native $REF = $COMMIT"
mkdir -p "$STAGE"
git -C $NATIVE bundle create "$STAGE/native.bundle" --all > /dev/null 2>&1
IMAGE_ID=$(docker image inspect $IMAGE --format '{{.Id}}')

cleanup() { docker rm -f $C > /dev/null 2>&1 || true; }
trap cleanup EXIT
docker create --name $C --memory 3100m --memory-swap 4100m $IMAGE sleep infinity > /dev/null
[ "$(docker inspect $C --format '{{len .Mounts}}')" = 0 ] || { echo "container has mounts; refusing"; exit 1; }
docker start $C > /dev/null
docker exec $C mkdir -p /home/builder/in
for f in "$STAGE/native.bundle" "$HERE/native_in_container.sh"; do
  docker cp "$(cygpath -m "$f")" $C:/home/builder/in/ > /dev/null
done
docker exec -u 0 $C chown -R builder /home/builder/in

echo "== warm (network on)"
docker exec $C bash /home/builder/in/native_in_container.sh warm "$COMMIT"

echo "== network cut"
for n in $(docker inspect $C --format '{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'); do
  docker network disconnect "$n" $C
done
docker exec $C bash -c 'getent hosts dl.google.com >/dev/null 2>&1 && exit 1; exit 0' || { echo "network still up"; exit 1; }

echo "== offline evidence build"
# Copy everything out before the container goes, pass or fail: a failed
# build's log is evidence too.
OFFLINE=0
docker exec $C bash /home/builder/in/native_in_container.sh offline "$COMMIT" || OFFLINE=$?
docker cp $C:/home/builder/out "$STAGE/out" > /dev/null
echo "image $IMAGE $IMAGE_ID" > "$STAGE/out/IMAGE.txt"
echo "staged in $STAGE"

[ -f "$STAGE/out/cleanroom-unsigned.aab" ] || { echo "no bundle came out"; exit 1; }
sha256sum "$HOST_AAB" "$STAGE/out/cleanroom-unsigned.aab"
python "$(cygpath -m "$HERE")/../../redteam-runs/20260929T2330Z-v1.0.8-7c2567c2/cleanroom/compare.py" \
  "$(cygpath -m "$HOST_AAB")" "$STAGE/out/cleanroom-unsigned.aab" --show 40 | tee "$STAGE/out/aab-compare.txt"
