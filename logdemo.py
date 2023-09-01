
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

lines  = dict()
errors = dict()
for i in range(0, _num_lines):
    lines[i]  = ""
    errors[i] = 0

def random_msg():
    num = random.randint(5, 25)
    msg = ""
    for i in range(0, num):
        msg = msg + chr(random.randint(32, 127))
    return msg

def _display(pos, msg, error):
    h = _height
    x = _start_x
    y = _start_y + pos * (h + 1)
    fg = LCD.GREEN
    bg = LCD.BLACK
    if error > 0:
        fg = LCD.YELLOW
    if error > 1:
        fg = LCD.RED
    lcd.rect(x, y, LCD.WIDTH, h+1, bg, True)
    lcd.text(msg, x, y, fg)

_pos = 0
def display(msg, error):
    global _pos
    lines[_pos]  = msg
    errors[_pos] = error
    _display(_pos, msg, error)
    _pos = _pos + 1
    if _pos >= _num_lines:
        _pos = _num_lines-1
        for i in range(0, _pos):
            lines[i]  = lines[i+1]
            errors[i] = errors[i+1]
            _display(i, lines[i], errors[i])
        _display(_pos, "", 0)
    lcd.show()
        
while True:
    display(random_msg(), random.randint(0, 3))
    time.sleep_ms(300)
    