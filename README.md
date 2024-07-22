# Simple Docker Flask Mqtt

## Softwares

- **Flask app**     : Mqtt Publisher
- **Mosquitto**     : Mqtt Broker/Server
- **ESP8266Client** : Mqtt Subscriber

## Requirements

You just need this 2 softwares:

- **Docker Engine**, and
- **Docker Compose**.

> More detail of docker installation: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

## Usage

If you're on Linux/Mac environment, just copy this following command:

```bash
chmod a+x run.sh && sudo bash run.sh
```

But, if you on Windows, just type the manual command (I recommend to use Git Bash):

```powershell
docker-compose up -d --build
```

Don't forget to upload esp8266 code to your own device. Also, change these variables to your own WiFi and Mqtt configuration:

```arduino
const char* ssid = "xxxxxxxxxxxx";
const char* pass = "xxxxxxxxxxxx";
const char* mqtt_server = "192.168.1.x";
const int mqtt_port = 11884;
const char* sub_topic = "flask/mqtt";
```

## Thank's
