#!/bin/bash
# This lab is run on an Ubuntu 22.04.4 machine

apt-get update
# Installation of apache server if it is not already installed for Ubuntu system
if ! dpkg -l | grep -q apache2; then
    apt-get install -y apache2
fi
