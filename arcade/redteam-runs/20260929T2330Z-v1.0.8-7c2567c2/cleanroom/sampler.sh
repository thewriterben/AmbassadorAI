#!/system/bin/sh
# usage: sampler.sh <uid>
while true; do cat /proc/net/tcp /proc/net/tcp6 | awk -v u="$1" '$8==u {print $3}' >> /data/local/tmp/socks.txt; sleep 1; done
