#!/usr/bin/python3

from subprocess import check_output
import os
# store brightness variable
brightness = float( 
				check_output("xrandr --verbose | grep -m 1 -i brightness | cut -f2 -d ' '", 
				shell=True) 
				)
print('Brightness', brightness)
print(type(brightness))
if brightness < 1:
    final = brightness + 0.05
    if final > 1:
        final = 1
    os.system('xrandr --output eDP-1 --brightness {}'.format(final))

