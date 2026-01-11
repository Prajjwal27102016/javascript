import numpy
import matplotlib.pyplot as plt

xpoints = numpy.array([1, 8])
ypoints = numpy.array([3, 10])

plt.plot(xpoints, ypoints, "p",ms=10,mec="r",mfc="g")
plt.show()