import mariadb
import random
import time

connection = mariadb.connect(
    user="stmarys",
    password="5ch00l##",
    host="192.168.2.150",
    database="StMarysSchool_MariaDB")

#A cursor is a database object that retrieves and also updates data, one row at a time, from a set of data.
cursor = connection.cursor()

def add_data(device, student, status):
    try:
        statement = "INSERT INTO students (device, student, status) VALUES (%s, %s, %d)"
        data = (device, student, status)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")

for x in range(30):
    stations = ["pupil_station_1", "pupil_station_2", "pupil_station_3", "pupil_station_4", "pupil_station_5", "water_fountain", "playground", "panic_button", "pocket_module"]
    pupils = ["Alex", "Cameron", "Charlie", "Chris", "Daniel", "David", "Erin", "Isabel", "James", "Jessica", "John", "Joshua", "Lexi", "Lois", "Lucy", "Mary", "Max", "Michael", "Mimi", "Nathaniel", "Nicholas", "Olivia", "Paul", "Phoebe", "Rachel", "Ryan", "Sally", "Samantha", "Seb", "Susan" ]
    status = random.randint(1,5)
    pupil = random.choice(pupils)
    station = random.choice(stations)
    add_data(station, pupil, status)
connection.close()
