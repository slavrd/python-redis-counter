#!/usr/bin/env bash
# Install python prerequisites

# install requirements for the vagrant user
sudo su vagrant -c 'python3.7 -m pip install -r /vagrant/requirements.txt --user'
