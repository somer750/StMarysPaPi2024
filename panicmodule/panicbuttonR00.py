# import the needed libraries
from gpiozero import LED
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mariadb

GPIO.setmode(GPIO.BCM)
device = "PanicButton07" # set the device name, needs to be different for each device

# create an instance of the RFID reader:
rfid = SimpleMFRC522()

# set up the input pins (BCM Mode):
BTN1_PIN = 16
# set up the output pins (BCM Mode):
btn1Led = LED(4)

# enable the pull-up resistors
GPIO.setup(BTN1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# connect to the database
connection = mariadb.connect(
    user="stmarys",
    password="5ch00l##",
    host="192.168.2.150",
    database="StMarysSchool_MariaDB")

#A cursor is a database object that retrieves and also updates data, one row at a time, from a set of data.
cursor = connection.cursor()

nexttoggle = time.time() + 1


# function to add data to the database

def add_data(student): # function to read the button state and enter database record
    btn1Led.on()
    reject = False
    print("Card detected! Name = ", student)
    timeout = time.time() + 10 # allow maximum 10 seconds
    while True:
        if GPIO.input(BTN1_PIN) == GPIO.LOW:
                print("Panic Button was pressed")
                status = 6
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
    btn1Led.off()


# main logic loop below:

print("waiting for card")
try:
    while True:
        id, text = rfid.read_no_block()
        if id != None: # if a card has been detected...
            print("Card detected")
            add_data(text) # call the function to add data, and send the data read from the card
        if time.time()>nexttoggle:
                nexttoggle = time.time() + 0.5
                btn1Led.toggle()
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
