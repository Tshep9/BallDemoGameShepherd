import pygame, sys, math
from Wall import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newLines += [line]

    lines = newline


    print(lines)

loadLevel("Levels/level.lvl")