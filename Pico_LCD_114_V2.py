
#
#  based on https://www.waveshare.com/wiki/Pico-LCD-1.14
#
#  - runs with standard MicroPython 1.19 or later
#  - can be configured to use only part of the physical display to
#    save FrameBuffer memory if needed; the remaining vertical resp.
#    horizontal borders can be colored individually
#  - backlight intensity can be changed
#  - additional color definitions
#  - installable with mip.install("github:tacker66/Pico_LCD_114_V2")
#

from machine import Pin, SPI, PWM
import framebuf
import time

class LCD_114(framebuf.FrameBuffer):
    
    # Display size
    WIDTH  = 240
    HEIGHT = 135
    # Keys
    #      2         A
    #    4 3 6
    #      5         B
    KEY_A = 15
    KEY_B = 17
    KEY_2 = 2
    KEY_3 = 3
    KEY_4 = 16
    KEY_5 = 18
    KEY_6 = 20
    # Control lines
    DC  = 8
    CS  = 9
    RST = 12
    # SPI interface
    SCK = 10
    MOSI= 11
    # PWM line
    BL  = 13
    # RGB565 colors (see https://rgbcolorpicker.com/565; LSB first!)
    WHITE  = 0xffff
    BLACK  = 0x0000
    RED    = 0x00f8
    GREEN  = 0xe007
    BLUE   = 0x1f00
    YELLOW = 0x0cff
    
    def set_backlight(self, rate=None):
        if rate == None:
            return int(100 * self.pwm.duty_u16() / 65535.0 + 0.5)
        rate = int(rate)
        if rate < 0:
            rate = 0
        if rate > 100:
            rate = 100
        rate = int(rate / 100.0 * 65535.0)
        self.pwm.duty_u16(rate)
        
    def __init__(self, width=WIDTH, height=HEIGHT, v_border_color=0x0000, h_border_color=0x0000):
        if width < 0:
            width = 0
        if width > LCD_114.WIDTH:
            width = LCD_114.WIDTH
        if height < 0:
            height = 0
        if height > LCD_114.HEIGHT:
            height = LCD_114.HEIGHT
        self.width  = width
        self.height = height
        self.spi = SPI(1, 10_000_000, sck=Pin(LCD_114.SCK), mosi=Pin(LCD_114.MOSI))
        self.pwm = PWM(Pin(LCD_114.BL))
        self.pwm.freq(256)
        self.set_backlight(25)
        self.rst = Pin(LCD_114.RST, Pin.OUT)
        self.cs  = Pin(LCD_114.CS,  Pin.OUT)
        self.cs(1)
        self.dc  = Pin(LCD_114.DC,  Pin.OUT)
        self.dc(1)
        self.keyA = Pin(LCD_114.KEY_A, Pin.IN, Pin.PULL_UP)
        self.keyB = Pin(LCD_114.KEY_B, Pin.IN, Pin.PULL_UP)
        self.key2 = Pin(LCD_114.KEY_2,  Pin.IN, Pin.PULL_UP)
        self.key3 = Pin(LCD_114.KEY_3,  Pin.IN, Pin.PULL_UP)
        self.key4 = Pin(LCD_114.KEY_4, Pin.IN, Pin.PULL_UP)
        self.key5 = Pin(LCD_114.KEY_5, Pin.IN, Pin.PULL_UP)
        self.key6 = Pin(LCD_114.KEY_6, Pin.IN, Pin.PULL_UP)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        # vertical and horizontal borders
        self.border_buffer = bytearray(2)
        self.v_border_color = int(v_border_color)
        self.h_border_color = int(h_border_color)
        self.init_display()

    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        self.rst(1)
        self.rst(0)
        self.rst(1)
        self.write_cmd(0x36)
        self.write_data(0x70)
        self.write_cmd(0x3A) 
        self.write_data(0x05)
        self.write_cmd(0xB2)
        self.write_data(0x0C)
        self.write_data(0x0C)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x33)
        self.write_cmd(0xB7)
        self.write_data(0x35) 
        self.write_cmd(0xBB)
        self.write_data(0x19)
        self.write_cmd(0xC0)
        self.write_data(0x2C)
        self.write_cmd(0xC2)
        self.write_data(0x01)
        self.write_cmd(0xC3)
        self.write_data(0x12)
        self.write_cmd(0xC4)
        self.write_data(0x20)
        self.write_cmd(0xC6)
        self.write_data(0x0F) 
        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)
        self.write_cmd(0xE0)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2B)
        self.write_data(0x3F)
        self.write_data(0x54)
        self.write_data(0x4C)
        self.write_data(0x18)
        self.write_data(0x0D)
        self.write_data(0x0B)
        self.write_data(0x1F)
        self.write_data(0x23)
        self.write_cmd(0xE1)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0C)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2C)
        self.write_data(0x3F)
        self.write_data(0x44)
        self.write_data(0x51)
        self.write_data(0x2F)
        self.write_data(0x1F)
        self.write_data(0x1F)
        self.write_data(0x20)
        self.write_data(0x23)
        self.write_cmd(0x21)
        self.write_cmd(0x11)
        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x28)
        self.write_data(0x01)
        self.write_data(0x17)
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x35)
        self.write_data(0x00)
        self.write_data(0xBB)
        self.write_cmd(0x2C)
        self.cs(1)
        self.dc(1)
        self.cs(0)
        if self.width < LCD_114.WIDTH:
            self.border_buffer[0] = self.v_border_color % 256
            self.border_buffer[1] = self.v_border_color // 256
            ptr = 0
            for line in range(0, self.height):
                self.spi.write(self.buffer[ptr:ptr+2*self.width])
                ptr = ptr + 2*self.width
                for i in range(0, (LCD_114.WIDTH-self.width)*2, 2):
                    self.spi.write(self.border_buffer)
        else:
            self.spi.write(self.buffer)
        if self.height < LCD_114.HEIGHT:
            self.border_buffer[0] = self.h_border_color % 256
            self.border_buffer[1] = self.h_border_color // 256
            for line in range(0, LCD_114.HEIGHT-self.height):
                for i in range(0, LCD_114.WIDTH*2, 2):
                    self.spi.write(self.border_buffer)
        self.cs(1)
