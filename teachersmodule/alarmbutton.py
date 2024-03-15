# button_detection.py
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

BUTTON_PIN = 3
MQTT_broker = "192.168.2.150"
broker_port = 1883
topic = "alarm"


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client.connect(MQTT_broker, broker_port,3600)

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:
             print("Button Pressed")
             client.publish("alarm", "pressed")
             time.sleep(0.2)
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Goodbye!")

finally:
    print("Goodbye!")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
