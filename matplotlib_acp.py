import numpy
import matplotlib.pyplot as plt

xpoints = numpy.array([1, 8])
ypoints = numpy.array([3, 10])

plt.plot(xpoints, ypoints,linestyle='dashed',color='r')
plt.show()

wpoints = numpy.array([1, 8])
zpoints = numpy.array([3, 10])

plt.plot(wpoints, zpoints)
plt.show()


apoints = numpy.array([1, 8])
bpoints = numpy.array([3, 10])

plt.plot(apoints, bpoints,linestyle='dotted',color='b')
plt.show()


opoints = [0, 6]
ppoints = [0, 250]

plt.plot(opoints, ppoints)
plt.show()



points = numpy.array([1, 8])
lpoints = numpy.array([3, 10])

plt.plot(points, lpoints, "p",ms=10,mec="r",mfc="g")
plt.show()

import numpy
import matplotlib.pyplot as plt
y1= numpy.array([3, 8, 1, 10])
y2= numpy.array([4,5,6,7])
plt.plot(y1)
plt.plot(y2)
plt.show()