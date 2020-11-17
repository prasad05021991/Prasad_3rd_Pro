import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

x=np.linspace(norm.ppf(940),norm.ppf(1090),20)
plt.plot(x,norm.pdf(x),lw=5, alpha=0.6, label='norm pdf')
plt.show()
#x = norm(loc=1010, scale=20)

# PDF-probability density function
'''
y = (x-1010)/20
y1 = ((norm.pdf(y))/20)

#y = norm.pdf(x, loc=1010, scale=20)
print(x)
plt.plot(x, y1)
plt.show()
'''
