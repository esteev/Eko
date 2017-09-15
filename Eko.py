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
        # print("1")
        dictTemp1 = {}
        dictTemp1["unUsed"] = 100
        self.nitrogenCycle = Abiotics.NitrogenCycle(dictTemp1)
        dictTemp2 = {}
        dictTemp2["unUsed"] = 100
        self.waterCycle = Abiotics.WaterCycle(dictTemp2)
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
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        # Plot
        plt.pies = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title(chartName)
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


# print(self.nitrogenCycle.dict)

    def updatePie(self, val):
        plt.clf()
        risk = Slider(self.axarr, 'Risk', 0, 100.0, val)
        plt.show()
       # self.pies.clear()

eko = Eko()
eko.run()

