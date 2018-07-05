import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,2,100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.plot(x,y1,label='label1')
plt.plot(x,y2,color='pink',linewidth=3.0,linestyle='--',label='label2')
plt.xlabel('x')
plt.ylabel('y')
x_newticks = np.linspace(-2,2,5)
plt.xticks(x_newticks)
plt.yticks([-0.8,0,0.8],['low','median','high'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0.1))
plt.legend()

x0 = 1
y0 = np.sin(x0)
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[0,y0],'k--',linewidth=2.5)
plt.annotate(r'$sinx=%.4f$' % y0,xy=(x0,y0),xycoords='data',xytext=(+50,-50),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))
plt.text(1,-1,r'$this\ is\ a\ txet\ \alpha^2\ \sigma_i$',fontdict={'size':16,'color':'red'})

plt.show()
