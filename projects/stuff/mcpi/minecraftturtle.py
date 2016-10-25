#Minecraft Graphics Turtle
#Martin O'Hanlon
#www.stuffaboutcode.com

import time
import math
import blockslist as bl
from vec3 import Vec3
from util import *


class MinecraftTurtle:

    SPEEDTIMES = {0:0, 12:0.001, 11:0.01, 10:0.1, 9:0.2, 8:0.3, 7:0.4, 6:0.5, 5:0.6, 4:0.7, 3:0.8, 2:0.9, 1:1}

    def __init__(self, conn, position, player):
        #set defaults
        self.conn = conn
        self.target = player
        self.player = player
        #start position
        self.startposition = position
        #set turtle position
        self.position = position
        #set turtle angles
        self.heading = 0
        self.verticalheading = 0
        #set pen down
        self._pendown = True
        #set pen bl to black wool
        self._penbl = bl.Block(bl.WOOL.id, 15)
        #flying to true
        self.flying = True
        #set speed
        self.turtlespeed = 6
        #create turtle
        self.showturtle = True
        # set turtle bl
        self.turtlebl = bl.Block(bl.DIAMOND_BLOCK.id)
        # draw turtle
        self._drawTurtle(int(self.position.x), int(self.position.y), int(self.position.y))
        #previous vertical heading
        self.previous = 0
        #last turtle
        self.lastDrawnTurtle = Vec3(0,0,0)

    def forward(self, distance):
        #get end of line
        #x,y,z = self._findTargetBlock(self.position.x, self.position.y, self.position.z, self.heading, self.verticalheading, distance)
        x,y,z = self._findPointOnSphere(self.position.x, self.position.y, self.position.z, self.heading, self.verticalheading, distance)
        #move turtle forward
        self._moveTurtle(x,y,z)

    def backward(self, distance):
        #move turtle backward
        #get end of line
        #x,y,z = self._findTargetBlock(self.position.x, self.position.y, self.position.z, self.heading, self.verticalheading - 180, distance)
        x,y,z = self._findPointOnSphere(self.position.x, self.position.y, self.position.z, self.heading, self.verticalheading - 180, distance)
        #move turtle forward
        self._moveTurtle(x,y,z)

    def _moveTurtle(self,x,y,z):
        #get bls between current position and next
        targetx, targety, targetz = int(x), int(y), int(z)
        #if walking, set target Y to be height of world
        if self.flying == False: targety = int(self.conn.sendReceive("world.getHeight", intFloor(targetx, targetz)))
        currentx, currenty, currentz = int(self.position.x), int(self.position.y), int(self.position.z)
        #clear the turtle
        if self.showturtle: self._clearTurtle(self.lastDrawnTurtle.x, self.lastDrawnTurtle.y, self.lastDrawnTurtle.z)
        #if speed is 0 and flying, just draw the line, else animate it
        if self.turtlespeed == 0 and self.flying:
            #draw the line
            if self._pendown:
                # if block is list:
                #     blockData = block[1]
                #     block = block[0]
                # else:
                #     blockData = 0
                # if not absolute:
                #     s = conn.sendReceive("entity" + ".getTile", target)
                #     pos = Vec3(*map(int, s.split(",")))
                #     currentx += pos.x
                #     currenty += pos.y
                #     currentz += pos.z
                #     targetx = pos.x + targetx
                #     targety = pos.y + targety
                #     targetz = pos.z + targetz
                # list for vertices
                vertices = []
                # if the 2 points are the same, return single vertice
                if (currentx == targetx and currenty == targety and currentz == targetz):
                    vertices.append(Vec3(currentx, currenty, currentz))
                # else get all points in edge
                else:
                    dx = targetx - currentx
                    dy = targety - currenty
                    dz = targetz - currentz
                    ax = abs(dx) << 1
                    ay = abs(dy) << 1
                    az = abs(dz) << 1
                    sx = ZSGN(dx)
                    sy = ZSGN(dy)
                    sz = ZSGN(dz)
                    x = currentx
                    y = currenty
                    z = currentz
                    # x dominant
                    if (ax >= MAX(ay, az)):
                        yd = ay - (ax >> 1)
                        zd = az - (ax >> 1)
                        loop = True
                        while (loop):
                            vertices.append(Vec3(x, y, z))
                            if (x == targetx):
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
                            if (y == targety):
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
                            if (z == targetz):
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
                    self.conn.send("world.setBlock", intFloor(vertex.x,
                                                         vertex.y,
                                                         vertex.z,
                                                         self._penbl))
                # self.mcDrawing.drawLine(currentX, currentY - 1, currentZ, targetX, targetY - 1, targetZ, self._penbl.id, self._penbl.data)
        else:
            blsBetween = self.mcDrawing.getLine(currentx, currenty, currentz, targetx, targety, targetz)
            if self.verticalheading > 215 and self.verticalheading < 315:
                self.previous = -1
                for blBetween in blsBetween:
                    #if walking update the y, to be the height of the world
                    if self.flying == False: blBetween.y = int(self.conn.sendReceive("world.getHeight", intFloor(blBetween.x, blBetween.z)))
                    #check the material on the new turtle position
                    #replace = self.mc.getBlock(blBetween.x, blBetween.y, blBetween.z)
                    #draw the turtle
                    if self.showturtle: self._drawTurtle(blBetween.x, blBetween.y-2, blBetween.z)
                    #draw the pen
                    if self._pendown: self.conn.send("world.setBlock", intFloor(blBetween.x, blBetween.y - 1, blBetween.z, self._penbl.id, self._penbl.data))
                    #wait
                    time.sleep(self.SPEEDTIMES[self.turtlespeed])
                    #clear the turtle
                    if self.showturtle: self._clearTurtle(blBetween.x, blBetween.y-2, blBetween.z)
                #update turtle's position to be the target
                self.position.x, self.position.y, self.position.z = x,y,z
                #draw turtle
                if self.showturtle: self._drawTurtle(targetx, targety - 2, targetz)
            elif self.verticalheading > 45 and self.verticalheading < 135:
                self.previous = 1
                for blBetween in blsBetween:
                    #print blBetween
                    #if walking update the y, to be the height of the world
                    if self.flying == False: blBetween.y = int(self.conn.sendReceive("world.getHeight", intFloor(blBetween.x, blBetween.z)))
                    #draw the turtle
                    if self.showturtle: self._drawTurtle(blBetween.x, blBetween.y, blBetween.z)
                    #draw the pen
                    if self._pendown: self.conn.send("world.setBlock", intFloor(blBetween.x, blBetween.y - 1, blBetween.z, self._penbl.id, self._penbl.data))
                    #wait
                    time.sleep(self.SPEEDTIMES[self.turtlespeed])
                    #clear the turtle
                    if self.showturtle: self._clearTurtle(blBetween.x, blBetween.y, blBetween.z)
                #update turtle's position to be the target
                self.position.x, self.position.y, self.position.z = x,y,z
                #draw turtle
                if self.showturtle: self._drawTurtle(targetx, targety, targetz)
            else:
                if self.previous == -1:
                    for blBetween in blsBetween:
                        #print blBetween
                        #if walking update the y, to be the height of the world
                        if self.flying == False: blBetween.y = int(self.conn.sendReceive("world.getHeight", intFloor(blBetween.x, blBetween.z)))
                        #draw the turtle
                        if self.showturtle: self._drawTurtle(blBetween.x, blBetween.y-2, blBetween.z)
                        if self._pendown: self.conn.send("world.setBlock", intFloor(blBetween.x, blBetween.y - 1, blBetween.z, self._penbl.id, self._penbl.data))
                        time.sleep(self.SPEEDTIMES[self.turtlespeed])
                        if self.showturtle: self._clearTurtle(blBetween.x, blBetween.y-2, blBetween.z)
                        #self.mc.postToChat(-self.verticalheading)
                    #update turtle's position to be the target
                    self.position.x, self.position.y, self.position.z = x,y,z
                    #draw turtle
                    if self.showturtle: self._drawTurtle(targetx, targety - 2, targetz)
                else:
                    for blBetween in blsBetween:
                        #print blBetween
                        #if walking update the y, to be the height of the world
                        if self.flying == False: blBetween.y = int(self.conn.sendReceive("world.getHeight", intFloor(blBetween.x, blBetween.z)))
                        #draw the turtle
                        if self.showturtle: self._drawTurtle(blBetween.x, blBetween.y, blBetween.z)
                        if self._pendown: self.conn.send("world.setBlock", intFloor(blBetween.x, blBetween.y - 1, blBetween.z, self._penbl.id, self._penbl.data))
                        time.sleep(self.SPEEDTIMES[self.turtlespeed])
                        if self.showturtle: self._clearTurtle(blBetween.x, blBetween.y, blBetween.z)
                        #self.mc.postToChat(self.verticalheading)
                    #update turtle's position to be the target
                    self.position.x, self.position.y, self.position.z = x,y,z
                    #draw turtle
                    if self.showturtle: self._drawTurtle(targetx, targety, targetz)
                self.previous = 0


    def right(self, angle):
        #rotate turtle angle to the right
        self.heading = self.heading + angle
        if self.heading > 360:
            self.heading = self.heading - 360

    def left(self, angle):
        #rotate turtle angle to the left
        self.heading = self.heading - angle
        if self.heading < 0:
            self.heading = self.heading + 360

    def up(self, angle):
        #rotate turtle angle up
        self.verticalheading = self.verticalheading + angle
        if self.verticalheading > 360:
            self.verticalheading = self.verticalheading - 360
        #turn flying on
        if self.flying == False: self.flying = True

    def down(self, angle):
        #rotate turtle angle down
        self.verticalheading = self.verticalheading - angle
        if self.verticalheading < 0:
            self.verticalheading = self.verticalheading + 360
        #turn flying on
        if self.flying == False: self.flying = True

    def setx(self, x):
        self.setposition(x, self.position.y, self.position.z)

    def sety(self, y):
        self.setposition(self.position.x, y, self.position.z)

    def setz(self, z):
        self.setposition(self.position.x, self.position.y, z)

    def setposition(self, x, y, z, absolute=False):
        if not absolute:
            s = self.conn.sendReceive("entity" + ".getTile", self.target)
            pos = Vec3(*map(int, s.split(",")))
            #clear the turtle
            if self.showturtle:
                self._clearTurtle(self.position.x,
                                  self.position.y,
                                  self.position.z)
            #update the position
            self.position.x = pos.x + x
            self.position.y = pos.y + y
            self.position.z = pos.z + z
            #draw the turtle
            if self.showturtle:
                self._drawTurtle(self.position.x,
                                 self.position.y,
                                 self.position.z)
        else:
            #clear the turtle
            if self.showturtle:
                self._clearTurtle(self.position.x,
                                  self.position.y,
                                  self.position.z)
            #update the position
            self.position.x = x
            self.position.y = y
            self.position.z = z
            #draw the turtle
            if self.showturtle:
                self._drawTurtle(self.position.x,
                                 self.position.y,
                                 self.position.z)

    def setheading(self, angle):
        self.heading = angle

    def setverticalheading(self, angle):
        self.verticalheading = angle
        #turn flying on
        if self.flying == False: self.flying = True

    #def home(self):
        #self.position.x = startposition.x
        #self.position.y = startposition.y
        #self.position.z = startposition.z

    def pendown(self):
        self._pendown = True

    def penup(self):
        self._pendown = False

    def isdown(self):
        return self.pendown

    def fly(self):
        self.flying = True

    def walk(self):
        self.flying = False
        self.verticalheading = 0

    def penblock(self, blId, blData = 0):
        self._penbl = bl.Block(blId, blData)

    def speed(self, turtlespeed):
        self.turtlespeed = turtlespeed

    def _drawTurtle(self,x,y,z):
        #draw turtle
        self.conn.send("world.setBlock", intFloor(x, y, z, self.turtlebl.id, self.turtlebl.data))
        self.lastDrawnTurtle = Vec3(x,y,z)

    def _clearTurtle(self,x,y,z):
        #clear turtle
        self.conn.send("world.setBlock", intFloor(x, y, z, bl.AIR.id))

    def _findTargetBlock(self, turtleX, turtleY, turtleZ, heading, verticalheading, distance):
        x,y,z = self._findPointOnSphere(turtleX, turtleY, turtleZ, heading, verticalheading, distance)
        x = int(round(x,0))
        y = int(round(y,0))
        z = int(round(z,0))
        return x,y,z

    def _findPointOnSphere(self, cx, cy, cz, horizontalAngle, verticalAngle, radius):
        x = cx + (radius * (math.cos(math.radians(verticalAngle)) * math.cos(math.radians(horizontalAngle))))
        y = cy + (radius * (math.sin(math.radians(verticalAngle))))
        z = cz + (radius * (math.cos(math.radians(verticalAngle)) * math.sin(math.radians(horizontalAngle))))
        return x, y, z

    def _roundXYZ(self, x,y,z):
        return int(round(x,0)), int(round(y,0)), int(round(z,0))

    def _roundVec3(self, position):
        return Vec3(int(position.x), int(position.y), int(position.z))


