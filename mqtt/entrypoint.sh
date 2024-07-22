#!/bin/sh

# Change ownership of the data and log directories
chown -R mosquitto:mosquitto /mosquitto/data /mosquitto/log

# Change permissions of all files in /mosquitto/data to 0700
find /mosquitto/data -type f -exec chmod 0700 {} \;

# Start mosquitto
exec "$@"