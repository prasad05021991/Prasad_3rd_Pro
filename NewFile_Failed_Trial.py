import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import norm

#trial_1

x1=np.arange(-5,6,1)
y1=norm.pdf(x1,0,1)
print(y1)
plt.plot(x1,y1)
plt.show()

#trial_2

x=np.random.normal(loc=1020,scale=10,size=(11))
sns.distplot(x,hist=False)
plt.title('Weights Vs Number of bags')
plt.show()
print("X value:",x)

#trial_3

zScore=((x-x.mean())/x.std())
print("Z Value:",zScore)
sns.distplot(zScore,hist=False)
plt.title('Z-score vs Number of bags')
plt.show()

for x,z in zip(x,zScore):
    print("X and Z value:",x,z)

#trial_4

r=norm.rvs(size=100)
print("R value:",r)
sns,distplot(r,hist=False)
plt.show()
