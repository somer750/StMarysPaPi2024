# Headteacher's alarm function
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

# set up the input pins (BCM Mode):
muteBTN_PIN = 4
# set up the output pins (BCM Mode):
alarmBeacon = LED(3)

MQTT_broker = "192.168.2.150"
broker_port = 1883
topic = "alarm"


GPIO.setmode(GPIO.BCM)
GPIO.setup(muteBTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
     print("Message received: " + msg.payload.decode())
     if msg.payload.decode() == "pressed":
         print("sound the bell!")
         alarmBeacon.on()



client.connect(MQTT_broker, broker_port, 60)

client.loop_start()

client.on_connect = on_connect
client.on_message = on_message


try:
    while True:
        button_state = GPIO.input(muteBTN_PIN)
        if button_state == GPIO.LOW:
             print("Mute Button Pressed")
             alarmBeacon.off()
             time.sleep(0.2)
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Goodbye!")


finally:
    print("Goodbye!")
    GPIO.cleanup()
    client.loop_stop()
