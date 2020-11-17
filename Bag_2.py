import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#create range of x-values from -4 to 4 in increments of .001
x = np.arange(950, 1070, 20)

#create range of y-values that correspond to normal pdf with mean=1010 and SD=20
y = norm.pdf(x,1010,20)

#Adjust the machine settings to get the wheat bag filled with 1kg with mean=1010 and SD=3.33
y1 = norm.pdf(x,1010,3.33)

plt.plot(x,y)
plt.show()

plt.plot(x,y1)
plt.show()