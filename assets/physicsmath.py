import math


def freefall(g, t):
    return g * t


def timetofall(g, h):
    return math.sqrt((2*h)/g)


def getmeters(g, t):
    return (g * (t ** 2)) / 2
