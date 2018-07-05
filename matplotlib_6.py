import matplotlib.pyplot as plt
import numpy as np

a = np.random.random((3,4))*10

plt.figure()
plt.imshow(a,interpolation='nearest',cmap='hsv',origin='upper')
plt.colorbar(shrink=0.8)
plt.show()
