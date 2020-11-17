import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

#Creating a Bell Curve with only minimum range

x=np.linspace(-1000,1000,100)
y=norm.pdf(x)
plt.plot(x,y)
plt.show()
