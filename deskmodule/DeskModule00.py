# test7 had all buttons, LEDs and RFID working
# test8 is about adding database connectivity (this version works)
# test 9 is about tidying up the code, improving lights functionality. This version works!
# test 10 is refinements
# test 11 moved all the LEDs to the ULN2003A. Main impact is that  the common Anode RGB led logic needs to be reversed

# import the needed libraries
from gpiozero import LED
#from time import sleep, time
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mariadb

GPIO.setmode(GPIO.BCM)
device = "pupil_station_9" # set the device name, needs to be different for each device

# create an instance of the RFID reader:
rfid = SimpleMFRC522()

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
RGBG = LED(4)
RGBR = LED(18)

# enable the pull-up resistors
GPIO.setup(BTN1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN4_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN5_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# connect to the database
connection = mariadb.connect(
    user="stmarys",
    password="5ch00l##",
    host="192.168.2.150",
    database="StMarysSchool_MariaDB")

#A cursor is a database object that retrieves and also updates data, one row at a time, from a set of data.
cursor = connection.cursor()

nextchase = time.time() + 5

# function to add data to the database

def add_data(student): # function to read the button state and enter database record
    reject = False
    RGBG.off()
    RGBR.on()
    print("Card detected! Name = ", student)
    timeout = time.time() + 10 # allow maximum 10 seconds
    while True:
        if GPIO.input(BTN1_PIN) == GPIO.LOW:
                print("Button 1 was pressed")
                status = 1
                break
        elif GPIO.input(BTN2_PIN) == GPIO.LOW:
                print("Button 2 was pressed")
                status = 2
                break
        elif GPIO.input(BTN3_PIN) == GPIO.LOW:
                print("Button 3 was pressed")
                status = 3
                break
        elif GPIO.input(BTN4_PIN) == GPIO.LOW:
                print("Button 4 was pressed")
                status = 4
                break
        elif GPIO.input(BTN5_PIN) == GPIO.LOW:
                print("Button 5 was pressed")
                status = 5
                break
        elif timeout < time.time():
                reject = True
                break

    if reject == False:
        try:
                statement = "INSERT INTO students (device, student, status) VALUES (%s, %s, %d)"
                data = (device, student, status)
                cursor.execute(statement, data)
                connection.commit()
                print("Successfully added entry to database")
        except database.Error as e:
                print(f"Error adding entry to database: {e}")
    else:
            print("user timeout")


def chaser(): # function to animate the button leds
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



# main logic loop below:

try:
    while True:
        RGBG.on()
        RGBR.off()
        id, text = rfid.read_no_block()
        if id != None: # if a card has been detected...
            print("Card detected")
            add_data(text) # call the function to add data, and send the data read from the card
        
        if time.time()>nextchase:
                print("waiting for card")
                nextchase = time.time() + 5
                chaser()
        time.sleep(0.1)

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
