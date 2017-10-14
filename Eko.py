from Core import *
import Abiotics as Abiotics
import threading
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


class Eko(Core, object):
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

    def pond(self):
        self.waterCycle.showDict()
        self.nitrogenCycle.showDict()
        self.carbonCycle.showDict()

eko = Eko()
eko.run()

