# import the needed libraries
from gpiozero import LED
#from time import sleep, time
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
device = "pupil_station_9" # set the device name, needs to be different for each device

# set up the input pins (BCM Mode):
BTN1_PIN = 7
BTN2_PIN = 22
BTN3_PIN = 16
BTN4_PIN = 3
BTN5_PIN = 17
# set up the output pins (BCM Mode):
btn1Led = LED(5)
btn2Led = LED(6)
btn3Led = LED(13)
btn4Led = LED(19)
btn5Led = LED(27)
RGBR = LED(4)
RGBG = LED(18)

# enable the pull-up resistors
GPIO.setup(BTN1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN4_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN5_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# main logic loop below:

try:
    while True:

       if GPIO.input(BTN1_PIN) == GPIO.LOW:
                print("Button 1 was pressed")
       if GPIO.input(BTN2_PIN) == GPIO.LOW:
                print("Button 2 was pressed")
       if GPIO.input(BTN3_PIN) == GPIO.LOW:
                print("Button 3 was pressed")
       if GPIO.input(BTN4_PIN) == GPIO.LOW:
                print("Button 4 was pressed")
       if GPIO.input(BTN5_PIN) == GPIO.LOW:
                print("Button 5 was pressed")

       btn1Led.on()
#       btn1Led.off()
       btn2Led.on()
#       btn2Led.off()
       btn3Led.on()
#       btn3Led.off()
       btn4Led.on()
#       btn4Led.off()
       btn5Led.on()
       RGBG.on()
       RGBR.off()

except KeyboardInterrupt:
        print("Program halted by keyboard interrupt")

finally:
    print("Goodbye!")
    GPIO.cleanup()


'''
GPIO configuration noted here because of the endless problems finding a
combination that worked when using the RFID card and the other I/O pins!
GPIO 2 - causes problems
GPIO 3 - allocated to button 4
GPIO 4 - used for RGBR
GPIO 5 - used for LED 1
GPIO 6 - used for LED 2
GPIO 7 - allocated to button 1
GPIO 8 - is used for RFID reader
GPIO 9 - is used for RFID reader
GPIO 10 - is used for RFID reader
GPIO 11 - is used for RFID reader
GPIO 12 - causes problems
GPIO 13 - used for LED 3
GPIO 14 - causes problems
GPIO 15 - causes problems
GPIO 16 - allocated to button 3
GPIO 17 - is used for button 5
GPIO 18 - used for RGBG
GPIO 19 - used for LED 4
GPIO 20 - causes problems
GPIO 21 - causes problems
GPIO 22 - used for button 22
GPIO 23 - causes problems
GPIO 24 - causes problems
GPIO 25 - is used for RFID reader
GPIO 26 - causes problems
GPIO 27 - used for LED 5
"causes problems" means either the RFID card stops working, or the input reads false, or a compiler error
'''
