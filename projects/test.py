from stuff.pycraft import *

pos = where()
chat(pos)

move(3, 10, 5)

chat(where())

sphere(ice)

circle([wool, 5], direction="horizontal")

line(gold, 0, 0, 0, 0, 50, 0)

block(ice, y=3)

blocks(ice, x=5, y=6, z=10)

size = readnumber("tell the size...")

cube(redstone, size)

text = readstring("say something...")

chat("I said: " + text)

pyramid(sandstone)

polygon(obsidian, 12, 30)

# while True:
#     if over(ice):
#         chat("ice")
#         block(gold, y=-1)
#     if near(gold):
#         chat("gold nearby!")





# x = pos.x
# y = pos.y
# z = pos.z
# while True:
#     cube(ice, 5, x, y, z, absolute=True)
#     move(x-5, y+1, z+2, absolute=True)
#     time.sleep(0.1)
#     cube(air, 5, x, y, z, absolute=True)
#     x += 1

