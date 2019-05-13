#!/usr/bin/env bash
# Install/Setup python prerequisites

# install pip
sudo apt-get update >> /dev/null
sudo apt-get install -y python3-pip >> /dev/null

# install prerequisite python packages
pip3 install redis

