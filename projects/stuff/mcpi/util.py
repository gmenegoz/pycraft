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
