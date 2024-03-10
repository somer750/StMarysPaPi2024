  GNU nano 7.2                                      striptestR03.py                                                
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

#A cursor is a database object that retrieves and also updates data, one row at a time, from a set of data.
cursor = connection.cursor()


def get_data(studentquery):
    try:
      statement = "SELECT student, status FROM students WHERE student=%s ORDER BY record_id DESC"
      data = (studentquery,)
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
for x in range (1,6):
    print("Program will continue in ",6-x," seconds")
    time.sleep(1)


while True:
    James = get_data("James")
    print(James)
    get_data("ddddfer") # dummy test to see error handling
    break

cursor.close()
connection.close()
