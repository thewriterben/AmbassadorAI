# DGD app clean room. Nothing from the host's working copies enters this
# image; sources arrive later as git bundles via `docker cp`.
FROM eclipse-temurin:21-jdk-jammy

ENV ANDROID_HOME=/opt/android-sdk \
    ANDROID_SDK_ROOT=/opt/android-sdk \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends git unzip zip curl ca-certificates python3 xz-utils file binutils \
 && rm -rf /var/lib/apt/lists/*

# Google's command-line tools, the newest listed in Google's own repository manifest.
RUN set -e; \
    clt=$(curl -fsSL https://dl.google.com/android/repository/repository2-3.xml | grep -o 'commandlinetools-linux-[0-9]*_latest.zip' | sort -V | tail -1); \
    echo "$clt" > /opt/clt-version; \
    curl -fsSLo /tmp/clt.zip "https://dl.google.com/android/repository/$clt"; \
    mkdir -p $ANDROID_HOME/cmdline-tools /tmp/clt; unzip -q /tmp/clt.zip -d /tmp/clt; \
    mv /tmp/clt/cmdline-tools $ANDROID_HOME/cmdline-tools/latest; rm -rf /tmp/clt /tmp/clt.zip
ENV PATH=$PATH:/opt/android-sdk/cmdline-tools/latest/bin:/opt/android-sdk/platform-tools

# Exactly what the app's build declares: compileSdk 36, AGP 8.9.1's default
# build-tools 35.0.0, and the pinned NDK used to strip native libraries.
RUN yes | sdkmanager --licenses >/dev/null \
 && sdkmanager "platforms;android-36" "build-tools;35.0.0" "ndk;28.2.13676358" "platform-tools" >/dev/null \
 && chmod -R a+rwX $ANDROID_HOME

RUN useradd -m builder
USER builder
WORKDIR /home/builder
