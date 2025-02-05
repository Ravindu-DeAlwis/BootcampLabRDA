#!/bin/bash
# Check if Apache server is running
if systemctl is-active --quiet apache2; then
    # Stop Apache server
    sudo systemctl stop apache2
fi
