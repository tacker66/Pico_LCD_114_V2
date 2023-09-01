
from Pico_LCD_114_V2 import LCD_114 as LCD

lcd = LCD(width=230, height=125, v_border_color=LCD.GREEN, h_border_color=LCD.BLUE)
lcd.fill(LCD.BLACK)
lcd.show()

lcd.text("red", 90, 20, LCD.RED)
lcd.text("green", 90, 40, LCD.GREEN)
lcd.text("yellow", 90, 60, LCD.YELLOW)
lcd.text("blue", 90, 80, LCD.BLUE)
lcd.text("white", 90, 100, LCD.WHITE)

lcd.hline(10, 10, 220, LCD.BLUE)
lcd.hline(10, 125, 220, LCD.BLUE)
lcd.vline(10, 10, 115, LCD.BLUE)
lcd.vline(230, 10, 115, LCD.BLUE)
lcd.show()

while True:
    
    if lcd.keyA.value() == 0:
        lcd.fill_rect(208, 12, 20, 20, LCD.RED)
        lcd.v_border_color = LCD.RED
        lcd.h_border_color = LCD.YELLOW
        lcd.set_backlight(30)
    else:
        lcd.fill_rect(208, 12, 20, 20, LCD.WHITE)
        lcd.rect(208, 12, 20, 20, LCD.RED)

    if lcd.keyB.value() == 0:
        lcd.fill_rect(208, 103, 20, 20, LCD.RED)
        lcd.v_border_color = LCD.GREEN
        lcd.h_border_color = LCD.BLUE
        lcd.set_backlight(80)
    else:
        lcd.fill_rect(208, 103, 20, 20, LCD.WHITE)
        lcd.rect(208, 103, 20, 20, LCD.RED)

    if lcd.key2.value() == 0:
        lcd.fill_rect(37, 35, 20, 20, LCD.RED)
        lcd.set_backlight(lcd.set_backlight()+10)
    else:
        lcd.fill_rect(37, 35, 20, 20, LCD.WHITE)
        lcd.rect(37, 35, 20, 20, LCD.RED)

    if lcd.key3.value() == 0:
        lcd.fill_rect(37, 60, 20, 20, LCD.RED)
    else:
        lcd.fill_rect(37, 60, 20, 20, LCD.WHITE)
        lcd.rect(37, 60, 20, 20, LCD.RED)

    if lcd.key4.value() == 0:
        lcd.fill_rect(12, 60, 20, 20, LCD.RED)
    else:
        lcd.fill_rect(12, 60, 20, 20, LCD.WHITE)
        lcd.rect(12, 60, 20, 20, LCD.RED)

    if lcd.key5.value() == 0:
        lcd.fill_rect(37, 85, 20, 20, LCD.RED)
        lcd.set_backlight(lcd.set_backlight()-10)
    else:
        lcd.fill_rect(37, 85, 20, 20, LCD.WHITE)
        lcd.rect(37, 85, 20, 20, LCD.RED)

    if lcd.key6.value() == 0:
        lcd.fill_rect(62, 60, 20, 20, LCD.RED)
    else:
        lcd.fill_rect(62, 60, 20, 20, LCD.WHITE)
        lcd.rect(62, 60, 20, 20, LCD.RED)

    lcd.show()
