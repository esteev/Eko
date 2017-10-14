import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Open and load data from Abiotics.json
with open('Abiotics.json') as json_data:
    d = json.load(json_data)

fig1, ax1 = plt.subplots(len(d.keys()))

for index, cycle in enumerate(d):
	if d[cycle]["type"] == "piechart":
		labels = d[cycle]["tags"].keys()
		sizes = []
		for i, values in enumerate(d[cycle]["tags"]):
			sizes.append(d[cycle]["tags"][values]["value"])
		explode = (0, 0.1)
		ax1[index].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
		ax1[index].axis('equal') 

# def animate(i):
#     pullData = open("sampleText.txt","r").read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(int(x))
#             yar.append(int(y))
#     ax1.clear()
#     ax1.plot(xar,yar)
# ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()