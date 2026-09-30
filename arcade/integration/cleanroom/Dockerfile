# Base of the DGD clean room: JDK 21 and the Android SDK, nothing else.
# Nothing from the host's working copies enters this image; sources arrive as
# git bundles via `docker cp` when a container is created from it.
#
#   docker build -t dgd-cleanroom:1 -f Dockerfile .
#
# The image this was first built as: sha256:0ef9b2810304… (2026-09-29).
FROM eclipse-temurin:21-jdk-jammy

ENV ANDROID_HOME=/opt/android-sdk \
    ANDROID_SDK_ROOT=/opt/android-sdk \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends git unzip zip curl ca-certificates python3 xz-utils file binutils \
 && rm -rf /var/lib/apt/lists/*

# Google's command-line tools, pinned to the build the first image used.
ARG CLT=commandlinetools-linux-16111833_latest.zip
RUN set -e; echo "$CLT" > /opt/clt-version; \
    curl -fsSLo /tmp/clt.zip "https://dl.google.com/android/repository/$CLT"; \
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
