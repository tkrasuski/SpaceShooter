# -*- coding: utf-8 -*-
import pygame
from GameObjects import  Missile, Enemy, Rock, Ufo
import random

def getStuff(cnt):
    ret = []
    enecnt = random.randint(0,1)
    for i in range(enecnt):
        e = Enemy()
        x=random.randint(0, 9)
        e.rect.x=x*98
        ch = random.randint(1,100)
        if ch%7==0 and cnt%7==0:
            ret.append(e)
        if cnt%100==0:
            r = Rock()
            ret.append(r)
        if cnt%1000==0:
            u=Ufo()
            ret.append(u)
    return ret
