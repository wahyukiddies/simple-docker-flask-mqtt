FROM eclipse-mosquitto:latest

# Copy the mosquitto configuration file
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entry point
ENTRYPOINT ["/entrypoint.sh"]

# Command to start mosquitto
CMD ["mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]