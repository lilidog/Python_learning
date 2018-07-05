import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y1 = (1-x/float(12))*np.random.uniform(0.5,1,12)
y2 = (1-x/float(12))*np.random.uniform(0.5,1,12)

plt.figure()
plt.bar(x,y1,facecolor='#9999ff',edgecolor='white')
plt.bar(x,-y2,facecolor='#ff9999',edgecolor='white')
plt.ylim(-1.2,1.2)
plt.xticks(())
plt.yticks(())

for xx,yy in zip(x,y1):
    plt.text(xx,yy+0.02,'%.1f'% yy,ha='center',va='bottom')

for xx,yy in zip(x,y2):
    plt.text(xx,-yy-0.02,'-%.1f'% yy,ha='center',va='top')



plt.show()
