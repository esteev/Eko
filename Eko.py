from Core import *
#import Core as core
import Abiotics as Abiotics
import threading
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


class Eko(Core,object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = phosphorousCycle = sulphurCycle = None

    def init(self):
        super(Eko, self).init()
        dictTemp2 = {}
        dictTemp2["unUsed"] = 100
        self.waterCycle = Abiotics.WaterCycle(dictTemp2)
        dictTemp1 = {}
        dictTemp1["unUsed"] = 100
        self.nitrogenCycle = Abiotics.NitrogenCycle(dictTemp1)
        dictTemp3 = {}
        dictTemp3["unUsed"] = 100
        self.carbonCycle = Abiotics.CarbonCycle(dictTemp3)
        # self.phosphorousCycle = Abiotics.Resource(dictTemp)
        # self.sulphurCycle = Abiotics.Resource(dictTemp)

        self.pond()                                             # add more systems here

    def update(self, timePassed):
        self.gameTime += timePassed
        print(self.gameTime)

    def stop(self):
        Core._running = False

    def makePie(self, labels, sizes, explode, chartName):

        self.current_sizes = sizes
        self.current_explode = explode
        self.chartName = chartName
        self.current_labels = labels
        self.colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

        self.fig, self.axarr = plt.subplots(3)
        plt.subplots_adjust(left=0.25, bottom=0.25)
        
        # Plot
        plt.title(chartName)
        plt.axis([0, 1, -10, 10])
        self.axarr[0].pie(sizes, explode=explode, labels=labels, colors=self.colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        self.x = sizes
        self.axarr[0].set_position([0.25,0.3,.5,.5])
        self.axarr[2].set_position([0,0,0,0])

        self.axarr[1].set_position([0.1, 0.15, 0.8, 0.03])
        self.risk = Slider(self.axarr[1], labels[0] + labels[1], 0.0, sizes[0]+sizes[1], valinit=self.x[0])
        self.risk.on_changed(self.updatePie)
        # axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
        # self.make_picker(self.fig, self.x)
        plt.axis('equal')
        plt.show()

    def pond(self):
        self.waterCycle.showDict()
        self.makePie(self.waterCycle.returnLabels(), self.waterCycle.returnValues(), self.waterCycle.returnExplode()
                     , "Water Cycle")

        self.nitrogenCycle.showDict()
        self.makePie(self.nitrogenCycle.returnLabels(), self.nitrogenCycle.returnValues(),
                     self.nitrogenCycle.returnExplode(), "Nitrogen Cycle")

        self.carbonCycle.showDict()
        self.makePie(self.carbonCycle.returnLabels(), self.carbonCycle.returnValues(),
                      self.carbonCycle.returnExplode(), "Carbon Cycle")

    def make_picker(self, fig, wedges):

        def onclick(event):
            wedge = event.artist
            label = wedge.get_label()
            print label

        # Make wedges selectable
        for wedge in wedges:
            wedge.set_picker(True)

        fig.canvas.mpl_connect('pick_event', onclick)


# print(self.nitrogenCycle.dict)

    def updatePie(self, val):
        self.axarr[0].clear()
        consistant_sum = self.current_sizes[0] + self.current_sizes[1]
        self.current_sizes[0] = val
        self.current_sizes[1] = consistant_sum - val
        self.axarr[0].pie(self.current_sizes, explode=self.current_explode, labels=self.current_labels, colors=self.colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        self.fig.canvas.draw_idle()
       # self.pies.clear()

eko = Eko()
eko.run()

