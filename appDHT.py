
# Import modules

import time
import sqlite3
import Adafruit_DHT

dbname='sensorsData.db'

# time in seconds

sampleFreq = 2 


# get data from DHT sensor

def getDHTdata():	
	
	DHT22Sensor = Adafruit_DHT.DHT22
	DHTpin = 16
	hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
	
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
		logData (temp, hum)