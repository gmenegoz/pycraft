#inizializzo
# import mcpi.minecraft as minecraft
# import mcpi.minecraftstuff as minecraftstuff
# import mcpi.minecraftturtle as mt
# mc = minecraft.connection
# mcdrawing = minecraftstuff.MinecraftDrawing(mc)

# initialize
import time, random, math, os, collections
import mcpi.connection
import mcpi.block as block
from mcpi.vec3 import Vec3
conn = mcpi.connection.Connection("localhost", 4711)

# find the player
#players = mc.getPlayerEntityIds()
ids = conn.sendReceive("world.getPlayerIds")
players = map(int, ids.split("|"))
player = players[0]

#BLOCKS
air = block.AIR.id
stone = block.STONE.id
grass = block.GRASS.id
dirt = block.DIRT.id
cobblestone = block.COBBLESTONE.id
wood_planks = block.WOOD_PLANKS.id
sapling = block.SAPLING.id
bedrock = block.BEDROCK.id
water_flowing = block.WATER_FLOWING.id
water = block.WATER.id
water_stationary = block.WATER_STATIONARY.id
lava_flowing = block.LAVA_FLOWING.id
lava = block.LAVA.id
lava_stationary = block.LAVA_STATIONARY.id
sand = block.SAND.id
gravel = block.GRAVEL.id
gold_ore = block.GOLD_ORE.id
iron_ore = block.IRON_ORE.id
coal_ore = block.COAL_ORE.id
wood = block.WOOD.id
leaves = block.LEAVES.id
glass = block.GLASS.id
lapis_lazuli_ore = block.LAPIS_LAZULI_ORE.id
lapis_lazuli = block.LAPIS_LAZULI_BLOCK.id
sandstone = block.SANDSTONE.id
bed = block.BED.id
cobweb = block.COBWEB.id
grass_tall = block.GRASS_TALL.id
wool = block.WOOL.id
flower_yellow = block.FLOWER_YELLOW.id
flower_cyan = block.FLOWER_CYAN.id
mushroom_brown = block.MUSHROOM_BROWN.id
mushroom_red = block.MUSHROOM_RED.id
gold = block.GOLD_BLOCK.id
iron = block.IRON_BLOCK.id
stone_slab_double = block.STONE_SLAB_DOUBLE.id
stone_slab = block.STONE_SLAB.id
brick = block.BRICK_BLOCK.id
tnt = block.TNT.id
bookshelf = block.BOOKSHELF.id
moss_stone = block.MOSS_STONE.id
obsidian = block.OBSIDIAN.id
torch = block.TORCH.id
fire = block.FIRE.id
stairs_wood = block.STAIRS_WOOD.id
chest = block.CHEST.id
diamond_ore = block.DIAMOND_ORE.id
diamond = block.DIAMOND_BLOCK.id
crafting_table = block.CRAFTING_TABLE.id
farmland = block.FARMLAND.id
furnace_inactive = block.FURNACE_INACTIVE.id
furnace_active = block.FURNACE_ACTIVE.id
door_wood = block.DOOR_WOOD.id
ladder = block.LADDER.id
stairs_cobblestone = block.STAIRS_COBBLESTONE.id
door_iron = block.DOOR_IRON.id
redstone_ore = block.REDSTONE_ORE.id
snow = block.SNOW.id
ice = block.ICE.id
snow = block.SNOW_BLOCK.id
cactus = block.CACTUS.id
clay = block.CLAY.id
sugar_cane = block.SUGAR_CANE.id
fence = block.FENCE.id
glowstone = block.GLOWSTONE_BLOCK.id
stone_brick = block.STONE_BRICK.id
glass_pane = block.GLASS_PANE.id
melon = block.MELON.id
fence_gate = block.FENCE_GATE.id
glowing_obsidian = block.GLOWING_OBSIDIAN.id
nether_reactor_core = block.NETHER_REACTOR_CORE.id
monster_spawner = block.MONSTER_SPAWNER.id
standing_sign = block.STANDING_SIGN_BLOCK.id
rail = block.RAIL.id
lever = block.LEVER.id
sponge = block.SPONGE.id
pumpkin = block.PUMPKIN.id
netherrack = block.NETHERRACK.id
soul_sand = block.SOUL_SAND.id
jack = block.JACK.id
stained_glass = block.STAINED_GLASS.id
cobblestone_wall = block.COBBLESTONE_WALL.id
prismarine = block.PRISMARINE.id
sea_lantern = block.SEA_LANTERN.id
hay_bale = block.HAY_BALE.id
coal = block.COAL_BLOCK.id
magma = block.MAGMA_BLOCK.id
redstone = block.REDSTONE_BLOCK.id
stained_glass_pane = block.STAINED_GLASS_PANE.id
slime = block.SLIME_BLOCK.id
carpet = block.CARPET.id
redstone_torch = block.REDSTONE_TORCH.id
piston = block.PISTON.id
sticky_piston = block.STICKY_PISTON.id
dispenser = block.DISPENSER.id
note = block.NOTE_BLOCK.id
stone_pressure_plate = block.STONE_PRESSURE_PLATE.id
hopper = block.HOPPER.id
dropper = block.DROPPER.id
activator_rail = block.ACTIVATOR_RAIL.id
powered_rail = block.POWERED_RAIL.id
detector_rail = block.DETECTOR_RAIL.id
beacon = block.BEACON.id
emerald = block.EMERALD_BLOCK.id
emerald_ore = block.EMERALD_ORE.id
quartz = block.QUARTZ_BLOCK.id
barrier = block.BARRIER.id
###############################################################


# UTIL FUNCTIONS:
def intFloor(*args):
    return [int(math.floor(x)) for x in flatten(args)]


def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, basestring):
            for ee in flatten(e): yield ee
        else: yield e


# draw point
def drawPoint3d(x, y, z, blockType, blockData=0):
    conn.send("world.setBlock", intFloor(x, y, z, blockType, blockData))


#################################################################


# def chat(text):
#     mc.postToChat(text)

def chat(text):
    conn.send("chat.post", text)


# def where(target=player):
#     return mc.entity.getTilePos(target)

def where(target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    return Vec3(*map(int, s.split(",")))


# def move(x=0, y=0, z=0, target=player, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         x += pos.x
#         y += pos.y
#         z += pos.z
#     mc.entity.setTilePos(target, x, y, z)

def move(x=0, y=0, z=0, target=player, absolute=False):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    if not absolute:
        x += pos.x
        y += pos.y
        z += pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))
#
#
# def sphere(block, radius=10, x=0, y=0, z=0, absolute=False, hollow=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         x += pos.x
#         y += pos.y
#         z += pos.z
#     if not hollow:
#         mcdrawing.drawSphere(x, y, z, radius, block)
#     else:
#         mcdrawing.drawHollowSphere(x, y, z, radius, block)
#
def sphere(block, radius=10, x=0, y=0, z=0, absolute=False, hollow=False, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    if block is list:
        blockData = block[1]
        block = block[0]
    else:
        blockData=0
    if not absolute:
        x += pos.x
        y += pos.y
        z += pos.z
    if not hollow:
        for xd in range(radius * -1, radius):
            for yd in range(radius * -1, radius):
                for zd in range(radius * -1, radius):
                    if xd ** 2 + yd ** 2 + zd ** 2 < radius ** 2:
                        conn.send("world.setBlock", intFloor(x + xd, y + yd, z + zd, block, blockData))
    else:
        for xd in range(radius * -1, radius):
            for yd in range(radius * -1, radius):
                for zd in range(radius * -1, radius):
                    if (xd ** 2 + yd ** 2 + zd ** 2 < radius ** 2) and (xd ** 2 + yd ** 2 + zd ** 2 > (radius ** 2 - (radius * 2))):
                        conn.send("world.setBlock", intFloor(x + xd, y + yd, z + zd, block, blockData))
#
#
# def circle(block,
#            radius=10,
#            x=0, y=0, z=0,
#            direction="vertical",
#            absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         x += pos.x
#         y += pos.y
#         z += pos.z
#     if direction == "vertical":
#         mcdrawing.drawCircle(x, y, z, radius, block)
#     elif direction == "horizontal":
#         mcdrawing.drawHorizontalCircle(x, y, z, radius, block)

def circle(block,
           radius=10,
           x=0, y=0, z=0,
           direction="vertical",
           absolute=False,
           target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    if block is list:
        blockData = block[1]
        block = block[0]
    else:
        blockData=0
    if not absolute:
        x += pos.x
        y += pos.y
        z += pos.z
    if direction == "vertical":
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        xd = 0
        yd = radius
        conn.send("world.setBlock", intFloor(x, y + radius, z, block, blockData))
        conn.send("world.setBlock", intFloor(x, y - radius, z, block, blockData))
        conn.send("world.setBlock", intFloor(x + radius, y, z, block, blockData))
        conn.send("world.setBlock", intFloor(x - radius, y, z, block, blockData))
        while xd < yd:
            if f >= 0:
                yd -= 1
                ddf_y += 2
                f += ddf_y
            xd += 1
            ddf_x += 2
            f += ddf_x
            conn.send("world.setBlock", intFloor(x + xd, y + yd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x - xd, y + yd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x + xd, y - yd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x - xd, y - yd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x + yd, y + xd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x - yd, y + xd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x + yd, y - xd, z, block, blockData))
            conn.send("world.setBlock", intFloor(x - yd, y - xd, z, block, blockData))
    elif direction == "horizontal":
        f = 1 - radius
        ddf_x = 1
        ddf_z = -2 * radius
        xd = 0
        zd = radius
        conn.send("world.setBlock", intFloor(x, y, z + radius, block, blockData))
        conn.send("world.setBlock", intFloor(x, y, z - radius, block, blockData))
        conn.send("world.setBlock", intFloor(x + radius, y, z, block, blockData))
        conn.send("world.setBlock", intFloor(x - radius, y, z, block, blockData))

        while xd < zd:
            if f >= 0:
                zd -= 1
                ddf_z += 2
                f += ddf_z
            xd += 1
            ddf_x += 2
            f += ddf_x
            conn.send("world.setBlock", intFloor(x + xd, y, z + zd, block, blockData))
            conn.send("world.setBlock", intFloor(x - xd, y, z + zd, block, blockData))
            conn.send("world.setBlock", intFloor(x + xd, y, z - zd, block, blockData))
            conn.send("world.setBlock", intFloor(x - xd, y, z - zd, block, blockData))
            conn.send("world.setBlock", intFloor(x + zd, y, z + xd, block, blockData))
            conn.send("world.setBlock", intFloor(x - zd, y, z + xd, block, blockData))
            conn.send("world.setBlock", intFloor(x + zd, y, z - xd, block, blockData))
            conn.send("world.setBlock", intFloor(x - zd, y, z - xd, block, blockData))
#
#
# def line(block, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         mcdrawing.drawLine(pos.x,
#                            pos.y,
#                            pos.z,
#                            pos.x + x1,
#                            pos.y + y1,
#                            pos.z + z1,
#                            block)
#     else:
#         mcdrawing.drawLine(x1, y1, z1, x2, y2, z2, block)
#
#
# def block(block, x=0, y=0, z=0, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         x += pos.x
#         y += pos.y
#         z += pos.z
#     mc.setBlock(x, y, z, block)
#
#
# def blocks(block, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         mc.setBlocks(pos.x,
#                      pos.y,
#                      pos.z,
#                      pos.x + x1,
#                      pos.y + y1,
#                      pos.z + z1,
#                      block)
#     else:
#         mc.setBlocks(x1, y1, z1, x2, y2, z2, block)
#
#
# def cube(block, side=10, x=0, y=0, z=0, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         x += pos.x
#         y += pos.y
#         z += pos.z
#     mc.setBlocks(x, y, z, x + side - 1, y + side - 1, z + side - 1, block)
#
#
# def pyramid(block, width=10, x=0, y=0, z=0, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if width % 2 == 0:
#         width += 1
#     if not absolute:
#         x = x + pos.x
#         y = y + pos.y
#         z = z + pos.z
#     if width == 1:
#         mc.setBlock(x, y, z, block)
#     else:
#         mc.setBlocks(x, y, z, x + width - 1, y, z + width - 1, block)
#         pyramid(block, width - 2, x + 1, y + 1, z + 1, absolute=True)
#
#
# def turtle(block):
#     pos = mc.entity.getTilePos(player)
#     turtle = mt.MinecraftTurtle(mc, mcdrawing, pos, player)
#     turtle.penblock(block)
#     turtle.speed(10)
#     return turtle
#
#
# def over(block, target=player):
#     pos = mc.entity.getTilePos(player)
#     material = mc.getBlock(pos.x,
#                            pos.y - 1,
#                            pos.z)
#     if material == block:
#         return True
#
#
# def under(target=player):
#     pos = mc.entity.getTilePos(player)
#     material = mc.getBlock(pos.x,
#                            pos.y - 1,
#                            pos.z)
#     return material
#
#
# def what(x, y, z, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     if not absolute:
#         x += pos.x
#         y += pos.y
#         z += pos.z
#     material = mc.getBlock(x, y, z)
#     return material
#
#
# def near(block, radius=10):
#     pos = mc.entity.getTilePos(player)
#     #return mcdrawing.getInSphere(block, radius, pos)
#     blocks = mc.getBlocks(pos.x - radius,
#                           pos.y - radius,
#                           pos.z - radius,
#                           pos.x + radius,
#                           pos.y + radius,
#                           pos.z + radius)
#     for b in blocks:
#         if b == block:
#             return True
#
#
# def readnumber(text):
#     done = False
#     value = 0
#     while not done:
#         try:
#             value = int(inputFromChat(text))
#             done = True
#         except:
#             chat("Il valore inserito non e' un numero valido")
#     return value
#
#
# def readstring(text):
#     done = False
#     value = 0
#     while not done:
#         try:
#             value = inputFromChat(text)
#             done = True
#         except:
#             chat("Il valore inserito non e' valido")
#     return value
#
#
# def inputFromChat(text):
#     chat(text)
#     readDone = False
#     value = "0"
#     while not readDone:
#         for msg in mc.events.pollChatPosts():
#             value = msg.message
#             readDone = True
#             break
#         time.sleep(0.10)
#     return value
#
#
# def polygon(block, shape=6, side=10, x=0, y=0, z=0, absolute=False):
#     pos = mc.entity.getTilePos(player)
#     angle = 0
#     i = shape
#     side -= 1
#     if not absolute:
#         x = x + pos.x
#         y = y + pos.y
#         z = z + pos.z
#     startx = x
#     startz = z
#     while i > 0:
#         if i == 1:
#             targetx = startx
#             targetz = startz
#         else:
#             targetx = int(round(x + side * math.cos(angle), 0))
#             targetz = int(round(z + side * math.sin(angle), 0))
#         mcdrawing.drawLine(x, y, z, targetx, y, targetz, block)
#         angle += 2 * math.pi / shape
#         x = targetx
#         z = targetz
#         i -= 1
#
#
# def maze(csvpath, base=grass, wall=gold, obstacle=lava):
#   #apro il file del labirinto
#   f = open(csvpath, "r")
#
#   #ottengo la posizione del giocatore
#   pos = mc.entity.getTilePos(player)
#
#   #definisco la coordinata -z- di partenza
#   z = pos.z+1
#
#   #PER OGNI riga del file del labirinto...
#   for line in f.readlines():
#     #divido la riga dove ci sono le virgole ottenendo una lista di celle
#     data = line.split(",")
#
#     #ricomincio dalla posizione -x- originaria ad ogni ciclo del loop
#     x = pos.x+1
#
#     #PER OGNI cella nella lista...
#     for cell in data:
#       #SE la cella e' 0
#       if cell == "0":
#         #ALLORA, il blocco da posizionare sara' ARIA
#         blocco = air
#       elif cell == "2":
#         blocco = obstacle
#       #ALTRIMENTI GOLD
#       else:
#         blocco = wall
#
#       #posiziono il blocco stabilito
#       mc.setBlock(x, pos.y, z, blocco)
#       mc.setBlock(x, pos.y+1, z, blocco)
#
#       #costruisco il pavimento
#       mc.setBlock(x, pos.y-1, z, base)
#
#       #mi sposto di 1 sull'asse X
#       x = x + 1
#
#     #mi sposto di 1 sull'asse Z
#     z = z + 1


#class chatListener:
    #
    #
    #def __init__(self):
        #self.start()
    #
    #def start(self) :
        #self.run = True
        #self.thread = threading.Thread(target=self.listen)
        #self.thread.start()
        #
    #def listen(self) :
        #while self.run:
            #for msg  in mc.events.pollChatPosts():
                #mc.postToChat(msg.message)
            #time.sleep(0.10)
            #
    #def exit(self) :
        #self.run = False
    #
#chatl = chatListener()
