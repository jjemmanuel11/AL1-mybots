import numpy
import matplotlib.pyplot as mpb

backpoints = numpy.load("data/backLegSensorValues.npy")
frontpoints = numpy.load("data/frontLegSensorValues.npy")

mpb.plot(backpoints, label="Back Leg", linewidth = 4)
mpb.plot(frontpoints, label="Front Leg", linewidth = 2)

mpb.legend()
mpb.show()