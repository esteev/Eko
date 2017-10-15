import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('AbioticsData.json') as json_data:
    d = json.load(json_data)
fig, ax1 = plt.subplots(len(d.keys()))

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
			explode = (0, 0.1)
			ax1[index].clear()
			ax1[index].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
		        shadow=True, startangle=90)
			ax1[index].axis('equal') 
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
