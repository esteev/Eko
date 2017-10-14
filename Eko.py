from Core import *
from Weather import *
import Abiotics as Abiotics


class Eko(Core, object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = phosphorousCycle = sulphurCycle = None

    def init(self):
        super(Eko, self).init()
        self.cycleThreadInitializePond()
        self.showDeets()

    def update(self, timePassed):
        self.gameTime += timePassed
        print(self.gameTime)

    def stop(self):
        Core._running = False

    def showDeets(self):
        self.waterCycle.showDict()
        self.nitrogenCycle.showDict()
        self.carbonCycle.showDict()

    def cycleThreadInitializePond(self):
        dictTemp2 = {}
        dictTemp2["unUsed"] = 100
        self.waterCycle = Abiotics.WaterCycle(dictTemp2)

        dictTemp1 = {}
        dictTemp1["unUsed"] = 100
        self.nitrogenCycle = Abiotics.NitrogenCycle(dictTemp1)

        dictTemp3 = {}
        dictTemp3["unUsed"] = 100
        self.carbonCycle = Abiotics.CarbonCycle(dictTemp3)


eko = Eko()
eko.run()

