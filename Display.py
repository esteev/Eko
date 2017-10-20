import json
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('AbioticsData.json') as json_data:
    d = json.load(json_data)

val = int(math.ceil(len(d.keys())**0.5))
fig, ax1 = plt.subplots(len(d.keys()), 2)
fig.set_facecolor("#C6E886")
flag = 0

font = {'weight' : 'bold',
        'size'   : 25}

plt.rc('font', **font)

plt.figtext(0.47, 0.96, "EkO", fontsize='large', color='#ffffff', ha ='right')

font = {'size'   : 10}

plt.rc('font', **font)

def animate(i):
	with open('AbioticsData.json') as json_data:
	    d = json.load(json_data)
	for index, cycle in enumerate(d):
		if d[cycle]["type"] == "piechart":
			labels = d[cycle]["tags"].keys()
			sizes = []
			labels.remove('unUsed')
			for i, values in enumerate(d[cycle]["tags"]):
				if values == 'unUsed':
					continue
				sizes.append(d[cycle]["tags"][values]["value"])
			explode = [0] * (len(d[cycle]["tags"].keys()) - 1)
			ax1[index, 1].clear()
			ax1[index, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
		        shadow=True, startangle=90)
			ax1[index, 1].axis('equal')
			ax1[index, 0].set_visible(False)

def on_click(event):
    global flag
    ax = event.inaxes
    if ax is None:
        return
    if event.button is 1:
        if flag==1:
	    	return
        flag = 1
        animate(0)
        ax._orig_position = ax.get_position()
        ax.set_position([ax._orig_position.x0 - 0.5, 0.6, ax._orig_position.width*1.2, ax._orig_position.height*1.2])
    elif event.button is 3:
        flag = 0
        try:
            ax.set_position(ax._orig_position)
            for axis in event.canvas.figure.axes:
                axis.set_visible(True)
        except AttributeError:
            pass
    else:
        return
    event.canvas.draw()



# def dikhao():
fig.canvas.mpl_connect('button_press_event', on_click)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
