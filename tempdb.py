# See README.md for details, particularly on
# the "personal" import.
# 


import os
import glob
import time
import subprocess
import datetime
import MySQLdb as mdb
import sys
from personal import *

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
     
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
     
def read_temp_raw():
    catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines
     
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
	    time.sleep(0.2)
	    lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
	temp_string = lines[1][equals_pos+2:]
    	temp_c = float(temp_string) / 1000.0
    	temp_f = temp_c * 9.0 / 5.0 + 32.0
    	return temp_c, temp_f


def show_alive():
	return "Still alive: the time is %s" % datetime.datetime.today()


 

while True:
    print('%.3f Degrees F  %.3f Degrees C' % (read_temp()[1], read_temp()[0]))	
    print show_alive()
    
    try:
        con = mdb.connect(dbhost, logmein, passw, datab);
	cur = con.cursor()
	print "Connected to DB"
	
	cels = read_temp()[0]
	fahren = read_temp()[1]

	cur.execute(
		"""INSERT INTO temperature (degreesc, degreesf) VALUES (%s, %s)""" % (cels, fahren ) )
	con.commit()
	
	print "database updated"

	cur.execute("SELECT VERSION()")
   
        ver = cur.fetchone()

        print "db version: %s" % ver

    except mdb.Error, e:

        print "Oops! Error. -  %d: %s" % (e.args[0],e.args[1])

    finally:
	
    	if con:

        	con.close()
		print "connection closed"

	
    time.sleep(600)
