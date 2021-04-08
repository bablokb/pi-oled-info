pi-oled-info
============

A systemd-service implemented as a python3-script which
displays core system information (currently CPU-temperature and load)
on a small 0.91 OLED-display.


Installation
============

Just run

    git clone https://github.com/bablokb/pi-oled-info.git
    cd pi-oled_info
    sudo tools/install

The install-script installs prerequisites, copies all the files of the
project, creates a systemd-service and configures `/boot/config.txt`
for I2C if not already configured. In this case you have to reboot
your Pi to make everything work.


Credits
=======

This project uses the library `lib_oled.py` 
from <https://github.com/BLavery/lib_oled96> with some minor modifications
copied from <https://github.com/rm-hull/luma.oled/> to make it work for
a 128x32 instead of a 128x64 display.