
import random
import time

from Pico_LCD_114_V2 import LCD_114 as LCD

lcd = LCD()
lcd.fill(LCD.BLACK)
lcd.show()

_num_lines = 12
_height    = 10
_start_x   = 0
_start_y   = 0

def random_msg():
    num = random.randint(5, 25)
    msg = ""
    for i in range(0, num):
        msg = msg + chr(random.randint(32, 127))
    return msg

def _display(pos, msg, error):
    fg = LCD.GREEN
    bg = LCD.BLACK
    if error > 0:
        fg = LCD.YELLOW
    if error > 1:
        fg = LCD.RED
    h = _height + 1
    x = _start_x
    y = _start_y + pos * h
    lcd.rect(x, y, LCD.WIDTH, h, bg, True)
    lcd.text(msg, x, y, fg)

_pos = 0
def display(msg, error):
    global _pos
    _display(_pos, msg, error)
    _pos = _pos + 1
    if _pos >= _num_lines:
        lcd.scroll(0, -_height)
        _pos = _num_lines-1
        _display(_pos, "", 0)
    lcd.show()
        
while True:
    display(random_msg(), random.randint(0, 3))
    time.sleep_ms(300)
