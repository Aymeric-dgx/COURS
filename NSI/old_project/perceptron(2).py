import random
from matplotlib import pyplot

g1 = []
for _ in range(500):
    x = random.normalvariate(2, 0.5)
    y = random.normalvariate(2, 0.5)
    g1.append([x, y, 1, -1])

g2 = []
for _ in range(500):
    x = random.normalvariate(5, 0.5)
    y = random.normalvariate(4, 0.5)
    g2.append([x, y, 1, 1])

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

w = [1, -1, 0]  # & = 
x = []
y = []
for i in range(10):
    x.append(i)
    y.append(-(w[0]*i+w[2])/w[1])

pyplot.plot(x, y, 'g-')
pyplot.show()





