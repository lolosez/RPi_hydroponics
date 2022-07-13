from datetime import datetime
import cv2
import numpy as np
import time
import board
import adafruit_dht
import psutil
import schedule
import csv 
import pandas as pd
import datetime

def save_to_csv():
    pass

fields = ['Date/Time', 'Temp', 'Humditiy']
dt = []
deg = []
hum = []
dict = {'date-time': dt, 'Temp': deg, 'Hum': hum}

df = pd.DataFrame(dict)


# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)


while True:
    # schedule.every().day.at("09:00").do()
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        dt.append(datetime.datetime.now())
        deg.append(temp)
        hum.append(humidity)
        # print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        print(df)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)