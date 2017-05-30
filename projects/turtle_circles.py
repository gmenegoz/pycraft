from stuff.pycraft import *


color = 1
conta = 0

uga = Turtle([wool, color])
uga.up(90)

while True:
    uga.forward(5)
    uga.up(20)
    conta += 1
    if conta >= 18:
        uga.up(30)
        conta = 0
        uga.penblock([wool, color])
        color += 1
    if color > 12:
        color = 0
