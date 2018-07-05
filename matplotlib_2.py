import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.xlim(-4,4)
plt.ylim(-1,1)
plt.xticks(np.linspace(-4,4,9))
plt.yticks([-0.8,0,0.8],[r'$bad$',r'$normal$',r'$good$'])
plt.plot(x,y1,'m--',label=r'$y=sinx$',linewidth=2)
plt.plot(x,y2,'c-',label=r'$y=cosx$',linewidth=3)
plt.title(r'$\alpha_i\ \beta^2$')
plt.legend()

x0 = np.pi/4
y0 = np.sin(x0)
plt.plot([x0,x0],[-1,y0],'k--',linewidth=1.5)

plt.annotate(r'$cross\ point$',xy=(x0,y0),xycoords='data',
             xytext=(30,-30),textcoords='offset points',
             fontsize=14,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.1'))
plt.text(3,-0.5,r'$by\ zdb$',fontdict=dict(size=12,color='b'))

ax = plt.gca()
ax.spines['left'].set_color('red')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='red',alpha=0.8,zorder=2))
plt.show()
#plt.savefig(r'E:\python\lianxi\matplotlib/test1.png',dpi=500)
