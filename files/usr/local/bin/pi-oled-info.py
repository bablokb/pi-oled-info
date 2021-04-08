#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# pi-oled-info: display system information on a small 0.91 oled
#
# Author: Bernhard Bablok
# License: GPL3
#
# Website: https://github.com/bablokb/pi-oled-info
#
# ----------------------------------------------------------------------------

FONT_PATH  = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_SIZE  = 16
UPDATE_INT = 30 # seconds

import os
import time
from smbus import SMBus
from lib_oled96 import ssd1306
from PIL import ImageFont

# --- system temperature   ---------------------------------------------------

def get_cpu_temp():
  file = open("/sys/class/thermal/thermal_zone0/temp")
  temp = float(file.read()) / 1000
  file.close();
  return temp

# --- system load   ----------------------------------------------------------

def get_load():
 return os.getloadavg()[0]

# --- update display   -------------------------------------------------------

def update(draw,font):
  draw.rectangle([0,0,oled.width+1,oled.height+1],fill=0)
  y_off = 0
  draw.text((0, y_off), "CPU: {0:3.1f}°C".format(get_cpu_temp()),
                                               font=font,fill=1)
  y_off += 0.90*FONT_SIZE
  draw.text((0, y_off), "Load: {0:4.2f}".format(get_load()),
                                               font=font,fill=1)
  oled.display()

# --- main program   ---------------------------------------------------------

if __name__ == '__main__':
  i2cbus = SMBus(1)

  oled = ssd1306(i2cbus,height=32)
  draw = oled.canvas

  font = ImageFont.truetype(FONT_PATH,FONT_SIZE)

  while True:
    update(draw,font)
    time.sleep(UPDATE_INT)
