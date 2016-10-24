from stuff.pycraft import *


color = 1
while True:
    cube([wool, color], 4, x=-2, y=-5, z=-2)
    if color < 12:
        color = color + 1
    else:
        color = 0
    time.sleep(0.1)