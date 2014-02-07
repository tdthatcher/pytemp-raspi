pytemp-raspi

---------------

An experimental python script to interface with a Dallas DS18B20 OneWire
digital temperature sensor.  The data is sent (in C and F) to a MySQL 
database every ten minutes.

---------------

contents: tempdb.py, personal.py, README.md

uses: os, glob, time, subprocess, datetime, MySQLdb, sys

also imports personal.py

personal.py is where database credentials are stored. A dummy file has been provided.
Add your own server address, login, password, and database name.  The default
table is "temperature". I'll likely pull that out of the code and add it to personal.py
import later.

The table layout I'm using is simple: an auto-increment index, auto date/timestamp,
degreesC, and degreesF.  Pytemp-raspi only actually interacts with the latter two columns.

--------------
credit where credit is due:

The GPIO interface code is from the tutorial at: 

http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing

The MySQLdb code is modified from code at:
http://zetcode.com/db/mysqlpython/
