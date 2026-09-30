#!/usr/bin/env bash
# $1 = module dir, $2 = output name
cd "$1" && flutter clean >/dev/null 2>&1 && flutter pub get >/dev/null 2>&1 && flutter build aar --no-debug --no-profile --dart-define=DGD_APP_TAB=true --dart-define=DGD_DEMO=true > /home/builder/out/$2.log 2>&1; echo "$2 exit $?"
cp build/host/outputs/repo/co/digitalgold/arcade/module/flutter_release/1.0/flutter_release-1.0.aar /home/builder/out/$2.aar
