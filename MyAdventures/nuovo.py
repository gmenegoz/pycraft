from stuff.pycraft import *

while True:
    if over(grass):
        block(stone, 0, -1, 0)

#while True:
#    pos = mc.entity.getTilePos(player)
#    if mc.getBlock(pos.x, pos.y - 1, pos.z) == grass:
#        mc.setBlock(pos.x, pos.y - 1, pos.z, stone)



