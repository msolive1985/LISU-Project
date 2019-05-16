import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import pandas as pd
from sys import exit

def update_lines(num, data, line):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(data[0:2, :num])    
    line.set_3d_properties(data[2, :num])    
    return line

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Reading the data from a CSV file using pandas
#repo = pd.read_csv('data.csv',sep=',',header=0)
zdata = sorted([-0.03,0,0,0,0,-0.08,-0.16,0,0,-0.01,-0.03,-0.01,-0.13,-0.09,-0.11,-0.14,-0.14,0,0]) 
xdata = sorted([0,0.03,0.05,0,0.01,0.06,0.07,-0.02,-0.03,0,0,0,0,0,0,0,0,-0.01,-0.01])
ydata = sorted([-0.01,0,0,0.03,0.02,0,0,0,0,0,0,0,0,0,0,0,0,-0.01,-0.01])
data = np.array((xdata, ydata, zdata))
print data.shape[1]
#exit()

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
line = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])[0]

# Setting the axes properties
ax.set_xlim3d([-0.25, 0.25])
ax.set_xlabel('X')

ax.set_ylim3d([-0.25, 0.25])
ax.set_ylabel('Y')

ax.set_zlim3d([-0.25, 0.25])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, data.shape[1], fargs=(data, line), interval=200, blit=False)

plt.show()
