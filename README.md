# Pico_LCD_114_V2

An enhanced driver for the [WaveShare Pico LCD 1.14](https://www.waveshare.com/wiki/Pico-LCD-1.14)

* runs with standard MicroPython 1.19 or later
* can be configured to use only part of the physical display to save FrameBuffer memory if needed; the remaining vertical resp.  horizontal borders can be colored individually
* backlight intensity can be changed
* additional color definitions
* demo code moved out of the driver file
* extended demos
  * graphicdemo.py: original demo code with additional demo of borders and backlight intensity
  * logdemo.py: textual log screen demo
  * fractaldemo.py: compute the mandelbrot set 
* installable with mip.install("github:tacker66/Pico_LCD_114_V2")
