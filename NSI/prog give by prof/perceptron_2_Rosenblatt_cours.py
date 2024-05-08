# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:06:51 2023

@author: Justine
"""

import random
import matplotlib as mpl
from matplotlib import pyplot
import math

def prod3(vec1 : list, vec2 : list):
    v1 = vec1[0] * vec2[0]
    v2 = vec1[1] * vec2[1]
    v3 = vec1[2] * vec2[2]
    return v1 + v2 + v3

def mulvec(val : int, vec : list) :
    v1 = val * vec[0]
    v2 = val * vec[1]
    v3 = val * vec[2]
    return [v1, v2, v3]

def addvec(vec1 : list, vec2 : list):
    v1 = vec1[0] + vec2[0]
    v2 = vec1[1] + vec2[1]
    v3 = vec1[2] + vec2[2]
    return [v1, v2, v3]

#Create two samples
#g1 = [[random.normalvariate(2, 0.5), random.normalvariate(2, 0.8), 1, 1] for _ in range(500)]
g1 = []
for _ in range(500):
    x = random.normalvariate(2, 0.5)
    y = random.normalvariate(2, 0.5)
    g1.append([x, y, 1, -1])
#g2 = [[random.normalvariate(5, 0.5), random.normalvariate(5, 0.5), 1, -1] for _ in range(500)]
g2 = []
for _ in range(500):
    x = random.normalvariate(5, 0.5)
    y = random.normalvariate(4, 0.5)
    g2.append([x, y, 1, 1])

#Create a super base
g = g1+g2
#Random the basse
sg = random.sample(g, len(g))

#----------Plot purpose :----------#
x1 = []
y1 = []
x2 = []
y2 = []
for i in range(len(g1)):
    x1.append(g1[i][0])
    y1.append(g1[i][1])
    x2.append(g2[i][0])
    y2.append(g2[i][1])

pyplot.plot(x1, y1, 'r*')
pyplot.plot(x2, y2, 'b+')

w = [1, -1, 0]
#w = [0, 1, 1]
x = []
y = []
for i in range(10):
    x.append(i)
    y.append(-(w[0]*i+w[2])/w[1])

pyplot.plot(x, y, 'g-')
#----------------------------------#

#------------#
# Perceptron #
#------------#
loop = 0
erreur = 1
while erreur > 0.0000001 and loop < 10000:
    loop = loop + 1
    err = 0
    for index in range(300):
        pred = prod3(w, sg[index][:3])
        if pred * sg[index][3] <= 0:
            update = mulvec(sg[index][3], sg[index][:3])
            w = addvec(w, update)
            err = err + 1
    erreur = err / len(g)

print(loop)
print(erreur)
print(w)

x = []
y = []
for i in range(10):
    x.append(i)
    y.append(-(w[0]*i+w[2])/w[1])

pyplot.plot(x, y, 'm-')
pyplot.show()