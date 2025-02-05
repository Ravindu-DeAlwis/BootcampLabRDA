#!/bin/bash
# Commands to validate the service is running correctly
echo "Running ValidateService hook"
# Example: Check the status of the web server
if curl -s --head http://localhost | grep "200 OK" > /dev/null; then
   echo "Application is running"
   exit 0
else
   echo "Application is not running"
   exit 1
fi