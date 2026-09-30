#!/usr/bin/env bash
# Step 3a: reproduce the rc2 Play bundle in a fresh dgd-cleanroom:1 container, offline.
set -uo pipefail
export MSYS_NO_PATHCONV=1
S="$(cygpath -m "$LOCALAPPDATA/Temp/rt108/step3")"; N=rt108-native-rc2
docker rm -f $N >/dev/null 2>&1
docker run -d --name $N --memory 3100m --memory-swap 4100m dgd-cleanroom:1 sleep infinity >/dev/null
echo "mounts: $(docker inspect $N --format '{{len .Mounts}}')"
docker exec $N mkdir -p /home/builder/in
docker cp "$S/native-rc2.bundle" $N:/home/builder/in/native.bundle >/dev/null
docker cp "$S/native_rep.sh" $N:/home/builder/native_rep.sh >/dev/null
docker exec -u 0 $N chown -R builder /home/builder/in /home/builder/native_rep.sh
echo "== warm (network on)"; docker exec -e TAG=android-1.0.8-rc2 $N bash /home/builder/native_rep.sh warm
echo "== cut"; docker network disconnect bridge $N; docker exec $N bash -c 'getent hosts dl.google.com >/dev/null 2>&1 && echo "NETWORK STILL UP" || echo "network cut: no DNS"'
echo "== offline"; docker exec -e TAG=android-1.0.8-rc2 $N bash /home/builder/native_rep.sh offline
docker exec $N bash -c 'grep -h "Arcade embed" /home/builder/out/*.log | head -2'
docker exec $N bash -c "stat -c \"gradlew mode %A\" /home/builder/native/android/gradlew; cd /home/builder/native/android && ./gradlew --version >/dev/null 2>&1 && echo \"./gradlew runs directly (P4)\""
mkdir -p "$S/out"; docker cp $N:/home/builder/out/. "$S/out/" >/dev/null
docker rm -f $N >/dev/null && echo "container removed"
