import time
import board
from adafruit_funhouse import FunHouse

funhouse = FunHouse(default_bg=0x000F20, scale=3)

funhouse.display.show(None)
text_row_one = funhouse.add_text(text="Happy", text_position=(12, 18), text_color=0x606060)
text_row_two = funhouse.add_text(text="Halloween", text_position=(12, 30), text_color=0x606060)
text_row_three = funhouse.add_text(text="Nos Calan", text_position=(12, 48), text_color=0x606060)
text_row_four = funhouse.add_text(text="Gaeaf", text_position=(12, 60), text_color=0x606060)
funhouse.display.show(funhouse.splash)

while True:
    print("hello!")
    time.sleep(30)
