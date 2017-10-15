import json
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('AbioticsData.json') as json_data:
    d = json.load(json_data)
val = int(math.ceil(len(d.keys())**0.5))
fig, ax1 = plt.subplots(len(d.keys()), 2)
flag = 0

def animate(i):
	# Open and load data from AbioticsData.json
	with open('AbioticsData.json') as json_data:
	    d = json.load(json_data)
	for index, cycle in enumerate(d):
		if d[cycle]["type"] == "piechart":
			labels = d[cycle]["tags"].keys()
			sizes = []
			for i, values in enumerate(d[cycle]["tags"]):
				sizes.append(d[cycle]["tags"][values]["value"])
			explode = [0] * len(d[cycle]["tags"].keys())
			ax1[index, 1].clear()
			ax1[index, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
		        shadow=True, startangle=90)
			ax1[index, 1].axis('equal')
			ax1[index, 0].set_visible(False)

def on_click(event):
    ax = event.inaxes
    if flag==0:
		return
    if ax is None:
        # Occurs when a region not in an axis is clicked...
        return
    if event.button is 1:
        flag = 1
        # On left click, zoom the selected axes
        animate(0)
        ax._orig_position = ax.get_position()
        ax.set_position([ax._orig_position.x0 - 0.5, 0.6, ax._orig_position.width*1.2, ax._orig_position.height*1.2])
        # for axis in event.canvas.figure.axes:
        #     # Hide all the other axes...
        #     if axis is not ax:
        #         axis.set_visible(True)
    elif event.button is 3:
        # On right click, restore the axes
        try:
            ax.set_position(ax._orig_position)
            for axis in event.canvas.figure.axes:
                axis.set_visible(True)
        except AttributeError:
            # If we haven't zoomed, ignore...
            pass
    else:
        # No need to re-draw the canvas if it's not a left or right click
        return
    event.canvas.draw()



# def dikhao():
fig.canvas.mpl_connect('button_press_event', on_click)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
