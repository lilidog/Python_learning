import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0,1,1024)
y = np.random.normal(0,1,1024)
T = np.arctan2(y,x)

plt.scatter(x,y,s=75,c=T,alpha=0.5)
plt.xlim(-2,2)
plt.ylim(-2,2)

plt.show()
