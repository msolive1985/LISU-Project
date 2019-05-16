from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

#bricks_translation x
#h = sorted([0.63,0.68,1,1,-1,-1,0,0,0,0,0,0,0,0,0,0])
#bricks_translation y
#h = sorted([0,0,0,0,0,0,-1,-1,1,1,1,1,1,1,-0.99,-1])
#bricks_translation z
#h = sorted([0,0,0,0,0,0,0.1,0.1,0,0,0,0,0,0,0.1,0.1])
#addrotation x
#h = sorted([0,0.03,0.05,0,0.01,0.06,0.07,-0.02,-0.03,0,0,0,0,0,0,0,0,-0.01,-0.01])
#addrotation y
#h = sorted([-0.01,0,0,0.03,0.02,0,0,0,0,0,0,0,0,0,0,0,0,-0.01,-0.01])
#addrotation z
#h = sorted([-0.03,0,0,0,0,-0.08,-0.16,0,0,-0.01,-0.03,-0.01,-0.13,-0.09,-0.11,-0.14,-0.14,0,0])

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
#zline = np.linspace(0, 15, 1000)
#xline = np.sin(zline)
#yline = np.cos(zline)
#ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = np.array(sorted([-0.03,0,0,0,0,-0.08,-0.16,0,0,-0.01,-0.03,-0.01,-0.13,-0.09,-0.11,-0.14,-0.14,0,0])) #15 * np.random.random(100)
xdata = np.array(sorted([0,0.03,0.05,0,0.01,0.06,0.07,-0.02,-0.03,0,0,0,0,0,0,0,0,-0.01,-0.01])) #np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.array(sorted([-0.01,0,0,0.03,0.02,0,0,0,0,0,0,0,0,0,0,0,0,-0.01,-0.01])) #np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

plt.show()
 
