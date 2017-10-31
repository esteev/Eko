import Abiotics.Abiotics as Abiotics
from Biotics.Biotic import *
from Buffer import *
from collections import OrderedDict
from Core import *
import json
from utils.jsonManager import *
import Abiotics.Weather as Weather


class Eko(Core, object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = oxygenCycle = phosphorousCycle = sulphurCycle = foreCaster = jansankhya = None
    buffer = dataFileAbiotics = None
    maintainer = {}

    def init(self):
        super(Eko, self).init()
        #   self.bufferStarter()
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

        self.janwarDekhioRe(timePassed)

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

                # print json.dumps(labels)
                # print json.dumps(sizes)

    def saveValuesToJSON(self):
        data = OrderedDict()
        save = jsonManager()

        # waterCycle
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

        self.maintainer = save.saveData(data, self.maintainer)

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

        self.maintainer = {}
        self.maintainer['water_cycle'] = {}
        self.maintainer['nitrogen_cycle'] = {}
        self.maintainer['carbon_cycle'] = {}
        self.maintainer['oxygen_cycle'] = {}
        self.maintainer['phosphorous_cycle'] = {}
        self.maintainer['sulphur_cycle'] = {}

        for z in self.waterCycle.returnLabels():
            self.maintainer['water_cycle'][z] = []

        for z in self.nitrogenCycle.returnLabels():
            self.maintainer['nitrogen_cycle'][z] = []

        for z in self.carbonCycle.returnLabels():
            self.maintainer['carbon_cycle'][z] = []

        for z in self.oxygenCycle.returnLabels():
            self.maintainer['oxygen_cycle'][z] = []

        for z in self.phosphorousCycle.returnLabels():
            self.maintainer['phosphorous_cycle'][z] = []

        for z in self.sulphurCycle.returnLabels():
            self.maintainer['sulphur_cycle'][z] = []

    def evaporation(self, timePassed):
        rate = self.foreCaster.heat.intensityVal
        self.waterCycle.resourceEvaporate(rate * timePassed)
        self.nitrogenCycle.resourceEvaporate(rate * timePassed)
        self.carbonCycle.resourceEvaporate(rate * timePassed)
        self.oxygenCycle.resourceEvaporate(rate * timePassed)
        self.phosphorousCycle.resourceEvaporate(rate * timePassed)
        self.sulphurCycle.resourceEvaporate(rate * timePassed)
        self.foreCaster.changeHumidity(rate * timePassed * 6)

    def precipitation(self):
        rate = self.foreCaster.moisture.humidVal
        NUMBER_OF_CYCLES = 6
        if rate > self.foreCaster.humidTolerance:
            self.waterCycle.resourcePrecipitate(rate / NUMBER_OF_CYCLES)
            self.nitrogenCycle.resourcePrecipitate(rate / NUMBER_OF_CYCLES)
            self.carbonCycle.resourcePrecipitate(rate / NUMBER_OF_CYCLES)
            self.oxygenCycle.resourcePrecipitate(rate / NUMBER_OF_CYCLES)
            self.phosphorousCycle.resourcePrecipitate(rate / NUMBER_OF_CYCLES)
            self.sulphurCycle.resourcePrecipitate(rate / NUMBER_OF_CYCLES)
            self.foreCaster.changeHumidity(-rate)

    def bufferStarter(self):
        self.buffer = Buffer(3, 3, 3)
        self.buffer.printer()

    # called at the start
    def spawnerPond(self):
        self.jansankhya = Jansankhya(20, 15, 10, 5, 3, 2, 1)

    # called whenever population is to be increased
    def instPopulation(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount,
                       storkCount):
        self.jansankhya.populator(algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount,
                                  bigFishyCount, storkCount)

    def janwarDekhioRe(self, timePassed):

        self.jansankhya.organismListShuffler()
        for x in self.jansankhya.organismList:
            foodState = 0
            currentRank = x.getFoodChainRank()
            for y in self.jansankhya.organismList:
                if y.getFoodChainRank() + 1 == currentRank:
                    # dealing with deleting eaten object
                    if (x.currentHunger >= x.hungerTolerance):
                        self.jansankhya.Koroshimasu(y)  # death by becoming breakfast
                        foodState = 1
                    break
                if y.getMaturity() == 1:
                    self.jansankhya.birth(y)
                    y.resetLibido()
                if y.shouldAlive() == 1:
                    self.jansankhya.Koroshimasu(y)      # death by age
                    print ("died of age")
            aliveStatus = x.update(timePassed, foodState)
            if aliveStatus == 1:
                self.jansankhya.Koroshimasu(x)          # death by hunger

        self.jansankhya.organismListUpdater()
        self.jansankhya.printer()
        self.jansankhya.totalPopPrint()
     #   self.jansankhya.popPrintDetailed()

    def configuration(self, humidTolerance):
        self.foreCaster.humidTolerance = humidTolerance


eko = Eko()
eko.run()
