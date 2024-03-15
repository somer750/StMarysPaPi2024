# import the needed libraries
from gpiozero import LED
#from time import sleep, time
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# set up the input pins (BCM Mode):
muteBTN_PIN = 4
# set up the output pins (BCM Mode):
alarmBeacon = LED(3)

#configure the inpput pin
GPIO.setup(muteBTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# main logic loop below:

try:
    while True:

       if GPIO.input(muteBTN_PIN) == GPIO.LOW:
                print("Button 1 was pressed")
                alarmBeacon.on()
                time.sleep(1)
       elif GPIO.input(muteBTN_PIN) == GPIO.HIGH:
                print("Button not pressed")
                alarmBeacon.off()
                time.sleep(1)

except KeyboardInterrupt:
        print("Program halted by keyboard interrupt")

finally:
    print("Goodbye!")
    GPIO.cleanup()
