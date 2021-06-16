import time
import board
from adafruit_funhouse import FunHouse
from adafruit_datetime import datetime, timedelta

funhouse = FunHouse()
funhouse.network.enabled = False
FEED = "temperature"
timestamp = datetime.now()

def log_data():
    funhouse.network.enabled = True
    funhouse.network.connect()
    funhouse.push_to_io(FEED, funhouse.peripherals.temperature)
    funhouse.network.enabled = False

while True:
    duration = datetime.now() - timestamp
    if duration >= timedelta(seconds=30):
        timestamp = datetime.now()
        log_data()
