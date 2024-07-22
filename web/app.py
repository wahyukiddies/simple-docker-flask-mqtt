from flask import Flask, render_template, request, redirect, url_for
from flask_mqtt import Mqtt

app = Flask(__name__)

# MQTT Configuration
app.config['MQTT_BROKER_URL'] = 'mosquitto'
app.config['MQTT_BROKER_PORT'] = 11884
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)

# Topic to publish and subscribe to
topic = 'flask/mqtt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publish', methods=['POST'])
def publish():
    message = request.form['message']
    mqtt.publish(topic, message)
    return redirect(url_for('index'))

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    print(f'Received message on topic {message.topic}: {payload}')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(topic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)