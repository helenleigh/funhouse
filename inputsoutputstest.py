import time
import board
import pwmio
import neopixel
from adafruit_motor import servo
from adafruit_funhouse import FunHouse
from adafruit_datetime import datetime, timedelta

funhouse = FunHouse()
pixel_pin = board.A2
num_pixels = 30
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)
pwm = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.1)

RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

while True:
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
        time.sleep(5)
