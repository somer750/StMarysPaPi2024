# you MUST use sudo privileges to run this program
# working version,reduced brightness in leds

import mariadb
import board
import neopixel
import time
import random
pixels = neopixel.NeoPixel(board.D18, 30)

# connect to the database
connection = mariadb.connect(
    user="stmarys",
    password="5ch00l##",
    host="192.168.2.150",
    database="StMarysSchool_MariaDB")

pupils = ["Alex", "Cameron", "Charlie", "Chris", "Daniel", "David", "Erin", "Isabel",
 "James", "Jessica", "John", "Joshua", "Lexi", "Lois", "Lucy", "Mary", "Max",
 "Michael", "Mimi", "Nathaniel", "Nicholas", "Olivia", "Paul", "Phoebe", "Rachel",
 "Ryan", "Sally", "Samantha", "Seb", "Susan" ]

#A cursor is a database object that retrieves and also updates data, one row at a time, from a set of data.
cursor = connection.cursor()

def get_data(studentquery):
    try:
      statement = "SELECT student, status FROM students WHERE student=%s ORDER BY record_id DESC"
      data = (studentquery,)
      connection.commit() # get any refreshed data
      cursor.execute(statement, data)
      row = cursor.fetchone()
      if row is not None: # this will only pull the very first result
        return(row[1])     # this returns the second part of the result, expressed as an integer
      else:
        print("no entry found")
    except mariadb.Error as e:
      print(f"Error retrieving entry from database: {e}")

# clear the display
for x in range(0, 30):
    pixels[x] = (0, 0, 0)
print("Display cleared. Press CTRL + C to stop the program")

# wait a short while to allow the user to cancel the program (in case they wanted to clear the screen)
for x in range (1,4):
    print("Program will continue in ",4-x," seconds")
    time.sleep(1)

while True:
    x=0 # reset the led number being illuminated before each pass
    for name in pupils:
        pupilmood = get_data(name)
        print(name,pupilmood)
        if pupilmood == 1:
            pixels[x] = (100, 0, 0)
        if pupilmood == 2:
            pixels[x] = (100,35,0)
        if pupilmood == 3:
            pixels[x] = (100,97,0)
        if pupilmood == 4:
            pixels[x] = (50,100,0)
        if pupilmood == 5:
            pixels[x] = (0,100,0)
        if pupilmood == 6:
            pixels[x] = (160, 32, 240)
        x=x+1 # increment the led number for each pass of the for loop

    time.sleep(5) # wait 5 seconds between database refreshes


cursor.close()
connection.close()
