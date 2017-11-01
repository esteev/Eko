import json
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Button

with open('./Data/AbioticsData.json') as json_data:
    d = json.load(json_data)

# val = int(math.ceil(len(d.keys())**0.5))
fig, ax1 = plt.subplots(3, 3)
fig.set_facecolor("#C6E886")
flag = 0

font = {'weight' : 'bold',
        'size'   : 25}

plt.rc('font', **font)

plt.figtext(0.47, 0.96, "EkO", fontsize='large', color='#ffffff', ha ='right')

font = {'size'   : 10}

plt.rc('font', **font)

def callback(event):
	print event


def animate(i):
	with open('./Data/AbioticsData.json') as json_data:
	    d = json.load(json_data)
	
	with open('./Data/LogData.json') as log_data:
	    k = json.load(log_data)

	# radio = []
	# for z in k:
	# 	for f in k[z]:
	# 		radio.append(z+ ' ' +f)
	# print radio
	# # radio button
	# rax = plt.axes([0.15, 0.05, 1, 1], facecolor='lightgoldenrodyellow')
	# radio2 = RadioButtons(rax, radio)
	
	# # plotting line graph
	ax1[2, 0].plot(k['water_cycle']['Biosphere'], color="r")
	axnext = plt.axes([0.25, 0.01, 0.05, 0.07])
	bnext = Button(axnext, 'Bda karo')
	bnext.on_clicked(callback)

	# plotting pie charts
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
			ax1[index%3, (index/3)+1].clear()
			ax1[index%3, (index/3)+1].set_title(cycle)
			ax1[index%3, (index/3)+1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
		        shadow=True, startangle=90)
			ax1[index%3, (index/3)+1].axis('equal')
			ax1[index%3, 0].set_visible(False)
	ax1[2, 0].set_visible(True)

def on_click(event):


    global flag
    ax = event.inaxes

    if ax is None:
        return

    if event.dblclick:
        animate(0)
        ax._orig_position = ax.get_position()
        print ax._orig_position

    elif event.button is 1:
        if flag==1:
	    	return
        flag = 1
        animate(0)
        ax._orig_position = ax.get_position()
        ax.set_position([0, 0.6, ax._orig_position.width*1.5, ax._orig_position.height*1.5])
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

def on_plot_hover(event):
	print event


# def dikhao():
# fig.canvas.mpl_connect('button_press_event', on_click)
# fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
