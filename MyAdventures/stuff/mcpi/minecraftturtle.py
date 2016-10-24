#Minecraft Graphics Turtle
#Martin O'Hanlon
#www.stuffaboutcode.com

import minecraft
import block
import time
import math
import collections


def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, basestring):
            for ee in flatten(e): yield ee
        else: yield e


def flatten_parameters_to_string(l):
    return ",".join(map(str, flatten(l)))


class MinecraftTurtle:

    SPEEDTIMES = {0:0, 12:0.001, 11:0.01, 10:0.1, 9:0.2, 8:0.3, 7:0.4, 6:0.5, 5:0.6, 4:0.7, 3:0.8, 2:0.9, 1:1}

    def __init__(self, mc, mcdrawing, position, player):
        #set defaults
        self.mc = mc
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
        #set pen block to black wool
        self._penblock = block.Block(block.WOOL.id, 15)
        #flying to true
        self.flying = True
        #set speed
        self.turtlespeed = 6
        #create turtle
        self.showturtle = True
        # create drawing object
        self.mcDrawing = mcdrawing
        # set turtle block
        self.turtleblock = block.Block(block.DIAMOND_BLOCK.id)
        # draw turtle
        self._drawTurtle(int(self.position.x), int(self.position.y), int(self.position.y))
        #previous vertical heading
        self.previous = 0
        #last turtle
        self.lastDrawnTurtle = minecraft.Vec3(0,0,0)

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
        #get blocks between current position and next
        targetX, targetY, targetZ = int(x), int(y), int(z)
        #if walking, set target Y to be height of world
        if self.flying == False: targetY = self.mc.getHeight(targetX, targetZ)
        currentX, currentY, currentZ = int(self.position.x), int(self.position.y), int(self.position.z)


        #clear the turtle
        if self.showturtle: self._clearTurtle(self.lastDrawnTurtle.x, self.lastDrawnTurtle.y, self.lastDrawnTurtle.z)

        #if speed is 0 and flying, just draw the line, else animate it
        if self.turtlespeed == 0 and self.flying:
            #draw the line
            if self._pendown: self.mcDrawing.drawLine(currentX, currentY - 1, currentZ, targetX, targetY - 1, targetZ, self._penblock.id, self._penblock.data)
        else:
            blocksBetween = self.mcDrawing.getLine(currentX, currentY, currentZ, targetX, targetY, targetZ)
            if self.verticalheading > 215 and self.verticalheading < 315:
                self.previous = -1
                for blockBetween in blocksBetween:
                    #if walking update the y, to be the height of the world
                    if self.flying == False: blockBetween.y = self.mc.getHeight(blockBetween.x, blockBetween.z)
                    #check the material on the new turtle position
                    #replace = self.mc.getBlock(blockBetween.x, blockBetween.y, blockBetween.z)
                    #draw the turtle
                    if self.showturtle: self._drawTurtle(blockBetween.x, blockBetween.y-2, blockBetween.z)
                    #draw the pen
                    if self._pendown: self.mcDrawing.drawPoint3d(blockBetween.x, blockBetween.y - 1, blockBetween.z, self._penblock.id, self._penblock.data)
                    #wait
                    time.sleep(self.SPEEDTIMES[self.turtlespeed])
                    #clear the turtle
                    if self.showturtle: self._clearTurtle(blockBetween.x, blockBetween.y-2, blockBetween.z)
                #update turtle's position to be the target
                self.position.x, self.position.y, self.position.z = x,y,z
                #draw turtle
                if self.showturtle: self._drawTurtle(targetX, targetY - 2, targetZ)
            elif self.verticalheading > 45 and self.verticalheading < 135:
                self.previous = 1
                for blockBetween in blocksBetween:
                    #print blockBetween
                    #if walking update the y, to be the height of the world
                    if self.flying == False: blockBetween.y = self.mc.getHeight(blockBetween.x, blockBetween.z)
                    #draw the turtle
                    if self.showturtle: self._drawTurtle(blockBetween.x, blockBetween.y, blockBetween.z)
                    #draw the pen
                    if self._pendown: self.mcDrawing.drawPoint3d(blockBetween.x, blockBetween.y - 1, blockBetween.z, self._penblock.id, self._penblock.data)
                    #wait
                    time.sleep(self.SPEEDTIMES[self.turtlespeed])
                    #clear the turtle
                    if self.showturtle: self._clearTurtle(blockBetween.x, blockBetween.y, blockBetween.z)
                #update turtle's position to be the target
                self.position.x, self.position.y, self.position.z = x,y,z
                #draw turtle
                if self.showturtle: self._drawTurtle(targetX, targetY, targetZ)
            else:
                if self.previous == -1:
                    for blockBetween in blocksBetween:
                        #print blockBetween
                        #if walking update the y, to be the height of the world
                        if self.flying == False: blockBetween.y = self.mc.getHeight(blockBetween.x, blockBetween.z)
                        #draw the turtle
                        if self.showturtle: self._drawTurtle(blockBetween.x, blockBetween.y-2, blockBetween.z)
                        if self._pendown: self.mcDrawing.drawPoint3d(blockBetween.x, blockBetween.y - 1, blockBetween.z, self._penblock.id, self._penblock.data)
                        time.sleep(self.SPEEDTIMES[self.turtlespeed])
                        if self.showturtle: self._clearTurtle(blockBetween.x, blockBetween.y-2, blockBetween.z)
                        #self.mc.postToChat(-self.verticalheading)
                    #update turtle's position to be the target
                    self.position.x, self.position.y, self.position.z = x,y,z
                    #draw turtle
                    if self.showturtle: self._drawTurtle(targetX, targetY - 2, targetZ)
                else:
                    for blockBetween in blocksBetween:
                        #print blockBetween
                        #if walking update the y, to be the height of the world
                        if self.flying == False: blockBetween.y = self.mc.getHeight(blockBetween.x, blockBetween.z)
                        #draw the turtle
                        if self.showturtle: self._drawTurtle(blockBetween.x, blockBetween.y, blockBetween.z)
                        if self._pendown: self.mcDrawing.drawPoint3d(blockBetween.x, blockBetween.y - 1, blockBetween.z, self._penblock.id, self._penblock.data)
                        time.sleep(self.SPEEDTIMES[self.turtlespeed])
                        if self.showturtle: self._clearTurtle(blockBetween.x, blockBetween.y, blockBetween.z)
                        #self.mc.postToChat(self.verticalheading)
                    #update turtle's position to be the target
                    self.position.x, self.position.y, self.position.z = x,y,z
                    #draw turtle
                    if self.showturtle: self._drawTurtle(targetX, targetY, targetZ)
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
            pos = self.mc.entity.getTilePos(self.player)
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

    def penblock(self, blockId, blockData = 0):
        self._penblock = block.Block(blockId, blockData)

    def speed(self, turtlespeed):
        self.turtlespeed = turtlespeed

    def _drawTurtle(self,x,y,z):
        #draw turtle
        self.mcDrawing.drawPoint3d(x, y, z, self.turtleblock.id, self.turtleblock.data)
        self.lastDrawnTurtle = minecraft.Vec3(x,y,z)

    def _clearTurtle(self,x,y,z):
        #clear turtle
        self.mcDrawing.drawPoint3d(x, y, z, block.AIR.id)

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

    def _roundXYZ(x,y,z):
        return int(round(x,0)), int(round(y,0)), int(round(z,0))

    def _roundVec3(position):
        return minecraft.vec3(int(position.x), int(position.y), int(position.z))


