
MAX_ITER  = 100
FREQUENCY = 240_000_000

import machine
machine.freq(FREQUENCY)

from Pico_LCD_114_V2 import LCD_114 as LCD
_lcd = LCD()
WIDTH  = LCD.WIDTH
HEIGHT = LCD.HEIGHT

def rgb888_2_rgb565(red, green, blue):
    val = (int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))
    hsb = val // 256
    lsb = val % 256
    return lsb * 256 + hsb
    
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n

RE_START = -2.1
RE_END   = 1
IM_START = -1.2
IM_END   = 1.2

for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        c = complex(RE_START+(x/WIDTH)*(RE_END-RE_START), IM_START+(y/HEIGHT)*(IM_END-IM_START))
        m = mandelbrot(c)
        color = 255 - int(m * 255 / MAX_ITER)
        _lcd.pixel(x, y, rgb888_2_rgb565(color, color, color))
    _lcd.show()
