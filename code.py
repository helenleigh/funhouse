import time
import board
import pwmio
import neopixel
from adafruit_motor import servo
from adafruit_funhouse import FunHouse
from adafruit_datetime import datetime, timedelta

funhouse = FunHouse(default_bg=0x000F20, scale=3)
pixel_pin = board.A2
num_pixels = 30
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)
pwm = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
FEED = "temperature"
funhouse.network.enabled = False

funhouse.display.show(None)
text_row_one = funhouse.add_text(text="Happy", text_position=(12, 18), text_color=0x606060)
text_row_two = funhouse.add_text(text="Halloween", text_position=(12, 30), text_color=0x606060)
text_row_three = funhouse.add_text(text="Nos Calan", text_position=(12, 48), text_color=0x606060)
text_row_four = funhouse.add_text(text="Gaeaf", text_position=(12, 60), text_color=0x606060)
funhouse.display.show(funhouse.splash)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.1)

def log_data():
    funhouse.network.enabled = True
    funhouse.network.connect()
    funhouse.push_to_io(FEED, funhouse.peripherals.temperature)
    funhouse.network.enabled = False

RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

timestamp = datetime.now()
while True:
    duration = datetime.now() - timestamp
    if duration >= timedelta(seconds=30):
        timestamp = datetime.now()
        log_data()
    if funhouse.peripherals.pir_sensor:
        my_servo.angle = 90
        time.sleep(1)
        color_chase(RED, 0.05)
        color_chase(YELLOW, 0.05)
        color_chase(GREEN, 0.05)
        color_chase(CYAN, 0.05)
        color_chase(BLUE, 0.05)
        color_chase(PURPLE, 0.05)
        color_chase(WHITE, 0.05)
        my_servo.angle = 0
        time.sleep(5)
    else:
        color_chase(OFF, 0.05)
        time.sleep(5)# Write your code here :-)
