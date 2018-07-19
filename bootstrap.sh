#!/usr/bin/env sh

export DEBIAN_FRONTEND=noninteractive

apt-get update && apt-get -y dist-upgrade

apt-get install -y \
    chromium-browser chromium-chromedriver \
    docker docker-compose \
    python3 tox
