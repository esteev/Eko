from Core import *
import Weather as Weather
import Abiotics as Abiotics
import json
from collections import OrderedDict
import Display as Display

class Eko(Core, object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = phosphorousCycle = sulphurCycle = foreCaster = None
    dataFileAbiotics = None

    def init(self):
        super(Eko, self).init()
        self.cycleThreadInitializePond()
        self.saveValuesToJSON()
        self.showDeets()
        Display.dikhao()

    def update(self, timePassed):
        self.gameTime += timePassed
        print(self.gameTime)
        self.jsonDataParser()
        self.foreCaster.update()
        self.saveValuesToJSON()

    def stop(self):
        Core._running = False

    def jsonDataParser(self):
        with open('AbioticsData.json') as json_data:
            self.dataFileAbiotics = json.load(json_data)
        count = 1
        for index, cycle in enumerate(self.dataFileAbiotics):
            dict = {}
            labels = self.dataFileAbiotics[cycle]["tags"].keys()
            sizes = []
            for i, values in enumerate(self.dataFileAbiotics[cycle]["tags"]):
                sizes.append(self.dataFileAbiotics[cycle]["tags"][values]["value"])
            for x, y in zip(labels, sizes):
                dict[x] = y

            if count == 1:
                self.waterCycle.resetValues(dict)
            elif count == 2:
                self.nitrogenCycle.resetValues(dict)
            elif count == 3:
                self.carbonCycle.resetValues(dict)
            count = count + 1
            print json.dumps(labels)
            print json.dumps(sizes)

    def saveValuesToJSON(self):
        data = OrderedDict()
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

        with open('AbioticsData.json', 'w') as outfile:
            json.dump(data, outfile)

    def showDeets(self):
        self.waterCycle.showDict()
        self.nitrogenCycle.showDict()
        self.carbonCycle.showDict()

    def cycleThreadInitializePond(self):
        self.waterCycle = Abiotics.WaterCycle()
        self.nitrogenCycle = Abiotics.NitrogenCycle()
        self.carbonCycle = Abiotics.CarbonCycle()
        self.foreCaster = Weather.Forecast()


eko = Eko()
eko.run()

