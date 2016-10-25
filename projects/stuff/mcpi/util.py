import collections
import math


# UTIL FUNCTIONS:
def intFloor(*args):
    return [int(math.floor(x)) for x in flatten(args)]


def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, basestring):
            for ee in flatten(e): yield ee
        else: yield e


def flatten_parameters_to_string(l):
    return ",".join(map(str, flatten(l)))


# return maximum of 2 values
def MAX(a, b):
    if a > b:
        return a
    else:
        return b


# return step
def ZSGN(a):
    if a < 0:
        return -1
    elif a > 0:
        return 1
    elif a == 0:
        return 0

# def drawPoint3d(x, y, z, blockType, blockData=0):
#     conn.send("world.setBlock", intFloor(x, y, z, blockType, blockData))


# def drawVertices(self, vertices, blockType, blockData=0):
#     for vertex in vertices:
#         conn.send("world.setBlock", intFloor(vertex.x,
#                                              vertex.y,
#                                              vertex.z,
#                                              blockType,
#                                              blockData))


def line(block, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, absolute=False, target=player):
    if block is list:
        blockData = block[1]
        block = block[0]
    else:
        blockData = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x1 += pos.x
        y1 += pos.y
        z1 += pos.z
        x2 = pos.x + x2
        y2 = pos.y + y2
        z2 = pos.z + z2
    # list for vertices
    vertices = []
    # if the 2 points are the same, return single vertice
    if (x1 == x2 and y1 == y2 and z1 == z2):
        vertices.append(Vec3(x1, y1, z1))
    # else get all points in edge
    else:
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        ax = abs(dx) << 1
        ay = abs(dy) << 1
        az = abs(dz) << 1
        sx = ZSGN(dx)
        sy = ZSGN(dy)
        sz = ZSGN(dz)
        x = x1
        y = y1
        z = z1
        # x dominant
        if (ax >= MAX(ay, az)):
            yd = ay - (ax >> 1)
            zd = az - (ax >> 1)
            loop = True
            while (loop):
                vertices.append(Vec3(x, y, z))
                if (x == x2):
                    loop = False
                if (yd >= 0):
                    y += sy
                    yd -= ax
                if (zd >= 0):
                    z += sz
                    zd -= ax
                x += sx
                yd += ay
                zd += az
        # y dominant
        elif (ay >= MAX(ax, az)):
            xd = ax - (ay >> 1)
            zd = az - (ay >> 1)
            loop = True
            while (loop):
                vertices.append(Vec3(x, y, z))
                if (y == y2):
                    loop = False
                if (xd >= 0):
                    x += sx
                    xd -= ay
                if (zd >= 0):
                    z += sz
                    zd -= ay
                y += sy
                xd += ax
                zd += az
        # z dominant
        elif (az >= MAX(ax, ay)):
            xd = ax - (az >> 1)
            yd = ay - (az >> 1)
            loop = True
            while (loop):
                vertices.append(Vec3(x, y, z))
                if (z == z2):
                    loop = False
                if (xd >= 0):
                    x += sx
                    xd -= az
                if (yd >= 0):
                    y += sy
                    yd -= az
                z += sz
                xd += ax
                yd += ay
    for vertex in vertices:
        conn.send("world.setBlock", intFloor(vertex.x,
                                             vertex.y,
                                             vertex.z,
                                             block,
                                             blockData))
