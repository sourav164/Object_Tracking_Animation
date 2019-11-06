'''
@author: Abdullah Sourav
The structure of script is based on @Sina's matplotlib animation tutorials ( https://bit.ly/2rfaxP3 )

The script is written to plot the locations of 7 tracked objects. By changing the number of data series [data, data2, data3,....] 
and output line [line, line2, line3,....], the script can be edited to track different number of objects.

'''

import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd
import numpy as np

# read data from csv file and drop the first row as it does not contain any location number but frame number
df = pd.read_csv("all_loc.csv")
df = df.drop(df.columns[0], 1)

# writer function initiation
Writer = animation.writers['ffmpeg']
writer = Writer(fps=14, metadata =dict(artist = "Me"), bitrate = -1)

# takes 7 data series and draw 7 lines
def update_line(num, data, line, data2, line2, data3, line3, data4, line4, data5, line5, data6, line6, data7, line7):
    line.set_data(data[...,:num])
    line2.set_data(data2[...,:num])
    line3.set_data(data3[...,:num])
    line4.set_data(data4[...,:num])
    line5.set_data(data5[...,:num])
    line6.set_data(data6[...,:num])
    line7.set_data(data7[...,:num])
    time_text.set_text("Frame: %.0f" % int(num))
    return line, line2, line3, line4, line5, line6, line7

# x, y locations of each object are converted into np.array
data = np.array([df.iloc[:,0].values,df.iloc[:,1].values])
data2 = np.array([df.iloc[:,2].values,df.iloc[:,3].values])
data3 = np.array([df.iloc[:,4].values,df.iloc[:,5].values])
data4 = np.array([df.iloc[:,6].values,df.iloc[:,7].values])
data5 = np.array([df.iloc[:,8].values,df.iloc[:,9].values])
data6 = np.array([df.iloc[:,10].values,df.iloc[:,11].values])
data7 = np.array([df.iloc[:,12].values,df.iloc[:,13].values])

# figure and line properties
fig = plt.figure()
ax = fig.add_subplot(111)
l, = ax.plot([], [], 'r-', label = "Steer 1")
k= ax.plot([], [], 'c-', label = "Steer 2")[0]
f= ax.plot([], [], 'y-', label = "Steer 3")[0]
a= ax.plot([], [], 'm-', label = "Steer 4")[0]
b= ax.plot([], [], 'k-', label = "Steer 5")[0]
c= ax.plot([], [], 'b-', label = "Steer 6")[0]
d= ax.plot([], [], 'g-', label = "Steer 7")[0]

# hide the axes marker and ticks 
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

# set the limit and add legends
ax.set_ylim(0,1440)
ax.set_xlim(0,1200)
ax.legend()

# create the video and save into the local directories
time_text = ax.text(0.1,0.95,"", transform = ax.transAxes, fontsize = 15, color="green")
line_ani = animation.FuncAnimation(fig, update_line, frames=500, fargs = (data, l, data2, k, data3, f, data4, a, data5,b, data6,c, data7, d))
plt.show()
line_ani.save("persp_500.mp4", writer= writer)
