import Abiotics as Abiotics
from Biotic import *
from Buffer import *
from collections import OrderedDict
from Core import *
import json
from jsonManager import *
import Weather as Weather

class Eko(Core, object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = oxygenCycle = phosphorousCycle = sulphurCycle = foreCaster = None
    buffer = dataFileAbiotics = None

    def init(self):
        super(Eko, self).init()
        self.bufferStarter()
        self.cycleThreadInitializePond()
        self.saveValuesToJSON()
        self.spawnerPond()
        self.showDeets()

    def update(self, timePassed):
        self.gameTime += timePassed
        print(self.gameTime)

        self.jsonDataParser()
        self.foreCaster.update()

        self.evaporation(timePassed)
        self.precipitation()

        self.saveValuesToJSON()

    def stop(self):
        Core._running = False

    def jsonDataParser(self):
        reader = jsonManager()
        self.dataFileAbiotics = reader.readFile()
        count = 1
        for index, cycle in enumerate(self.dataFileAbiotics):
            dict = {}
            labels = self.dataFileAbiotics[cycle]["tags"].keys()
            sizes = []
            for i, values in enumerate(self.dataFileAbiotics[cycle]["tags"]):
                sizes.append(self.dataFileAbiotics[cycle]["tags"][values]["value"])
            for x, y in zip(labels, sizes):
                dict[x] = y

            # if count == 1:
            #     self.waterCycle.resetValues(dict)
            # elif count == 2:
            #     self.nitrogenCycle.resetValues(dict)
            # elif count == 3:
            #     self.carbonCycle.resetValues(dict)
            # elif count == 4:
            #     self.oxygenCycle.resetValues(dict)
            # elif count == 5:
            #     self.phosphorousCycle.resetValues(dict)
            # elif count == 6:
            #     self.sulphurCycle.resetValues(dict)
            # count = count + 1
            
            print json.dumps(labels)
            print json.dumps(sizes)

    def saveValuesToJSON(self):
        data = OrderedDict()
        save = jsonManager()

        #waterCycle
        data['water_cycle'] = {'type': 'piechart'}
        tags = {}
        tagsTemp = self.waterCycle.returnLabels()
        valsTemp = self.waterCycle.returnValues()
        for k, v in zip(tagsTemp, valsTemp):
            tags[k] = {'value': str(v)}
        data['water_cycle']["tags"] = tags


        # nitrogenCycle
        data['nitrogen_cycle'] = {'type': 'piechart'}
        tags = {}
        tagsTemp = self.nitrogenCycle.returnLabels()
        valsTemp = self.nitrogenCycle.returnValues()
        for k, v in zip(tagsTemp, valsTemp):
            tags[k] = {'value': str(v)}
        data['nitrogen_cycle']["tags"] = tags

        # carbonCycle
        data['carbon_cycle'] = {'type': 'piechart'}
        tags = {}
        tagsTemp = self.carbonCycle.returnLabels()
        valsTemp = self.carbonCycle.returnValues()
        for k, v in zip(tagsTemp, valsTemp):
            tags[k] = {'value': str(v)}
        data['carbon_cycle']["tags"] = tags

        # oxygenCycle
        data['oxygen_cycle'] = {'type': 'piechart'}
        tags = {}
        tagsTemp = self.oxygenCycle.returnLabels()
        valsTemp = self.oxygenCycle.returnValues()
        for k, v in zip(tagsTemp, valsTemp):
            tags[k] = {'value': str(v)}
        data['oxygen_cycle']["tags"] = tags

        # phosphorousCycle
        data['phosphorous_cycle'] = {'type': 'piechart'}
        tags = {}
        tagsTemp = self.phosphorousCycle.returnLabels()
        valsTemp = self.phosphorousCycle.returnValues()
        for k, v in zip(tagsTemp, valsTemp):
            tags[k] = {'value': str(v)}
        data['phosphorous_cycle']["tags"] = tags

        # sulphurCycle
        data['sulphur_cycle'] = {'type': 'piechart'}
        tags = {}
        tagsTemp = self.sulphurCycle.returnLabels()
        valsTemp = self.sulphurCycle.returnValues()
        for k, v in zip(tagsTemp, valsTemp):
            tags[k] = {'value': str(v)}
        data['sulphur_cycle']["tags"] = tags

        save.saveData(data)

    def showDeets(self):
        self.waterCycle.showDict()
        self.nitrogenCycle.showDict()
        self.carbonCycle.showDict()

    def cycleThreadInitializePond(self):
        self.waterCycle = Abiotics.WaterCycle()
        self.nitrogenCycle = Abiotics.NitrogenCycle()
        self.carbonCycle = Abiotics.CarbonCycle()
        self.oxygenCycle = Abiotics.OxygenCycle()
        self.phosphorousCycle = Abiotics.PhosphorousCycle()
        self.sulphurCycle = Abiotics.SulphurCycle()
        self.foreCaster = Weather.Forecast()

    def evaporation(self, timePassed):
        rate = self.foreCaster.heat.intensityVal
        self.waterCycle.resourceEvaporate(rate*timePassed)
        self.nitrogenCycle.resourceEvaporate(rate*timePassed)
        self.carbonCycle.resourceEvaporate(rate*timePassed)
        self.foreCaster.changeHumidity(rate*timePassed*3)

    def precipitation(self):
        rate = self.foreCaster.moisture.humidVal
        if rate > self.foreCaster.humidTolerance:
            self.waterCycle.resourcePrecipitate(rate/3)
            self.nitrogenCycle.resourcePrecipitate(rate/3)
            self.carbonCycle.resourcePrecipitate(rate/3)
            self.foreCaster.changeHumidity(-rate)

    def bufferStarter(self):
        self.buffer = Buffer(10,10,10)
     #   self.buffer = Buffer(10)
     #   self.buffer.printer()

    def spawnerPond(self):
        algae = Algae("1", 1, 1, 0.01, 0, 5)
        catTail = CatTail("2", 2, 1, 0.1, 0, 5)
        zooPlankton = ZooPlankton("3", 1, 1, 0.01, 1, 5)
        tadpole = Tadpole("4", 3, 2, 0.2, 1.5, 5)
        smallFishy = GreenSunfish("5", 10, 5, 0.7, 2, 5)
        bigFishy = LargeBassMouth("6", 15, 7, 1, 3, 5)
        stork = Stork("7", 30, 10, 1.2, 4, 5)

eko = Eko()
eko.run()
