import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

try:
        while True:
            text = input ("Text to write : ")
            print ("Hold tag near the module...")
            id, text = rfid.write(text)
            print ("Written")
            print (id)
            print (text)
finally:
        print ("\ncleaning up")
        GPIO.cleanup()
