# import the needed libraries
from gpiozero import LED
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# set up the output pins (BCM Mode):
btn1Led = LED(5)
btn2Led = LED(6)
btn3Led = LED(13)
btn4Led = LED(19)
btn5Led = LED(27)

# main logic loop below:

try:
    while True:
        for x in range(5):
                btn1Led.on()
                time.sleep(0.08)
                btn2Led.on()
                btn1Led.off()
                time.sleep(0.08)
                btn3Led.on()
                btn2Led.off()
                time.sleep(0.08)
                btn4Led.on()
                btn3Led.off()
                time.sleep(0.08)
                btn5Led.on()
                btn4Led.off()
                time.sleep(0.08)
                btn5Led.off()
        time.sleep(2)
        for x in range(3):
                btn1Led.on()
                btn2Led.on()
                btn3Led.on()
                btn4Led.on()
                btn5Led.on()
                time.sleep(0.2)
                btn1Led.off()
                btn2Led.off()
                btn3Led.off()
                btn4Led.off()
                btn5Led.off()
                time.sleep(0.2)
        time.sleep(0.1)

except KeyboardInterrupt:
        print("Program halted by keyboard interrupt")

finally:
    print("Goodbye!")
    GPIO.cleanup()
