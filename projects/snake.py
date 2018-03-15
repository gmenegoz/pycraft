#!/usr/bin/python2
# -*- coding: utf-8 -*-

from pycraft_minetest import *

MELON = bl.MELON.id
STONE = bl.STONE.id
TNT = bl.TNT.id
DAMAGELOSS = 10
GAIN = 5
NEGGS = 10


class Snake:

    def __init__(self, position):
        self.position = position
        self.oldposition = self.position
        self.tail = []
        self.tailLength = 0
        self.points = 0

    def addtail(self, position):
        self.tailLength += 1
        self.tail.append(position)

    def movetail(self, position):
        position = position
        if self.tailLength > 1:
            block(air, self.tail[0].x, self.tail[0].y, self.tail[0].z, absolute=True)
            self.tail = self.tail[1:]
            self.tail.append(position)
            block([wool,6], position.x, position.y, position.z, absolute=True)

    def check(self):
        if over(MELON):

            return [where().x, where().y - 1, where().z]



class Egg:

    def __init__(self, x, y, z, kind=MELON):
        self.id = 0
        self.x = x
        self.y = y
        self.z = z
        self.position = Vec3(x, y, z)
        self.kind = kind

    def explode(self, snake):
        block(air, self.x, self.y, self.z, absolute=True)
        block(air, self.x, self.y - 1, self.z, absolute=True)
        snake.points -= DAMAGELOSS

    def create(self):
        block(self.kind, x=self.x, y=self.y, z=self.z, absolute=True)

    def eaten(self, snake):
        block(air, self.x, self.y, self.z, absolute=True)
        block(dirt, self.x, self.y - 1, self.z, absolute=True)
        snake.points += GAIN


class Arena:

    def __init__(self, size=50):
        self.pumpkins = 0
        self.stones = 0
        self.tnt = 0
        self.size = size
        self.gamer = None
        self.eggs = []
        self.inPos = where()  # TODO include target

    def create(self):
        blocks(grass,  - self.size / 2, - 1, 0, self.size / 2, - 1, + self.size)  # posiziona un prato
        blocks(air, - self.size / 2 - 20, 0, - 20, + self.size / 2 + 20, 50, + self.size + 20)  # svuota l'area di gioco
        blocks(fence, - self.size / 2, 0, 0, self.size / 2, 0, self.size)  # crea un recinto
        blocks(air, - self.size / 2 + 1, 0, 1, self.size / 2 - 1,  0, self.size - 1)  # svuota l'interno del recinto
        block(air, 0, 0, 0)  # crea un varco

    def popobject(self):
        x = self.inPos.x - self.size / 2 + random.randint(1, self.size - 1)
        z = self.inPos.z + random.randint(1, self.size - 1)
        odds = random.random()
        if odds > .9:
            kind = TNT
        elif odds > .8:
            kind = STONE
        else:
            kind = MELON
        egg = Egg(kind=kind, x=x, y=self.inPos.y, z=z)
        egg.create()
        return egg

    def whichegg(self, position):
        target = None
        for egg in self.eggs:
            if position.x == egg.x and position.y == egg.y + 1 and position.z == egg.z:
                target = egg
                break
        return target

    def present(self):
        chat("Benvenuto in Snakecraft")
        chat("Salta sui meloni per guadagnare punti. Evita il TNT!")
        chat("Le pietre non danno punteggio: danno solo fastidio")
        chat("Ad ogni nuovo melone mangiato ti si allunga la coda")
        chat("Non calpestarti la coda! Buona Fortuna")


area = Arena(size=30)
area.present()
area.create()
for i in range(NEGGS):
    egg = area.popobject()
    area.eggs.append(egg)
snake = Snake(where())
game = True

while game:
    snake.position = where()
    egg = area.whichegg(snake.position)
    if egg is not None:
        if egg.kind == TNT:
            egg.explode(snake)
            area.eggs.remove(egg)
        #  chat(str(snake.points) + " punti")
        elif egg.kind == MELON:
            egg.eaten(snake)
            area.eggs.remove(egg)
            snake.addtail(snake.oldposition)
           # chat(str(snake.points) + " punti")
        new = area.popobject()
        area.eggs.append(new)
    else:
        if snake.oldposition != snake.position:
            snake.movetail(snake.oldposition)
    snake.oldposition = snake.position
    if over(wool):
        game = False
    time.sleep(.1)

chat("Hai perso!")
