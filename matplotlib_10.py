import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

x = np.linspace(0,2*np.pi,200)
y = np.sin(x)

fig = plt.figure()
ax = plt.gca()
line, = ax.plot(x,y)

def my_sin(i):
    line.set_ydata(np.sin(x+i/10))
    return ax

def init():
    line.set_ydata(np.sin(x))
    return ax

ani = animation.FuncAnimation(fig=fig,func=my_sin,frames=100,init_func=init,interval=10,blit=False)
plt.show()
