import numpy as np
import matplotlib.pyplot as plt

Period = 10 #seconds
Time = np.linspace(0, Period, 1000)
ecc = 0.5

#Mean motion resonance
n = 2.0*np.pi/Time

a_R = 10.0

#Calculate the
Toleration = 1e-5
for t in Time:
    M = n*t
    print("The mean motion is:", M)

print("The toleration is given by:", Toleration")    
