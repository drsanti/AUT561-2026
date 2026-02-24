# Docker Setup for Week 06

This folder contains the configuration to run an **MQTT Broker** (Eclipse Mosquitto) using Docker Compose. This is required for the workshops in Week 06.

## 🧰 Files
*   `docker-compose.yml`: Defines the broker service and port mappings.
*   `mosquitto.conf`: Configuration file allowing anonymous access on port 1883.

## 🚀 How to Run

0.  Ensure **Docker Desktop** is running on your machine.
1.  Open your terminal in this folder (`AUT561/Week06/docker`).
2.  Start the broker:
    ```bash
    docker-compose up -d
    ```
3.  Verify the broker is running:
    ```bash
    docker ps
    ```
    You should see `mosquitto-broker` listening on port `1883`.

## 🛑 How to Stop
To stop and remove the container:
```bash
docker-compose down
```

## 📝 Troubleshooting
*   **Port 1883 is already in use:** Ensure no other MQTT broker (or a previous Docker container) is running on your machine.
*   **Docker not found:** Make sure **Docker Desktop** is installed and running.
