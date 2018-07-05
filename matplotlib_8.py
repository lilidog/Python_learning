import matplotlib.pyplot as plt

plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)

plt.show()
