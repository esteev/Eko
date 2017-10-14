from Core import *
import Weather as Weather
import Abiotics as Abiotics
import json


class Eko(Core, object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = phosphorousCycle = sulphurCycle = foreCaster = None
    dataFileAbiotics = None

    def init(self):
        super(Eko, self).init()
        self.cycleThreadInitializePond()
        self.showDeets()

    def update(self, timePassed):
        self.gameTime += timePassed
        print(self.gameTime)
    #    self.jsonDataParser()
        self.foreCaster.update()

    def stop(self):
        Core._running = False

    def jsonDataParser(self):
        with open('AbioticsData.json') as json_data:
            self.dataFileAbiotics = json.load(json_data)
        for index, cycle in enumerate(self.dataFileAbiotics):
            labels = self.dataFileAbiotics[cycle]["tags"].keys()
            sizes = []
            for i, values in enumerate(self.dataFileAbiotics[cycle]["tags"]):
                sizes.append(self.dataFileAbiotics[cycle]["tags"][values]["value"])

    #def saveDeets(self):


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

        self.foreCaster = Weather.Forecast()


eko = Eko()
eko.run()

