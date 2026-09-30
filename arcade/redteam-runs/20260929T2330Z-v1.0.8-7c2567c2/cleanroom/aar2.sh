#!/usr/bin/env bash
printf "org.gradle.jvmargs=-Xmx1024m -XX:MaxMetaspaceSize=640m -XX:ReservedCodeCacheSize=64m -XX:+UseSerialGC
org.gradle.workers.max=1
kotlin.compiler.execution.strategy=in-process
org.gradle.daemon=false
" > ~/.gradle/gradle.properties
cd /home/builder/dgd_arcade_module && flutter build aar --no-debug --no-profile --dart-define=DGD_APP_TAB=true --dart-define=DGD_DEMO=true > /home/builder/out/aar3.log 2>&1
echo "build aar exit $?"
grep -E "Built |What went wrong|disappeared" /home/builder/out/aar3.log | head -3
