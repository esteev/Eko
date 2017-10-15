#from collections import OrderedDict

class Resource:

    dict = {}

    def __init__(self, dictTemp):
        self.dict = dictTemp

    def resetValues(self, dictTemp):
        self.dict = dictTemp

    def resourceLeech(self, leechVal, leechTag, seedTag):
        self.dict[seedTag] = float(self.dict[seedTag]) - leechVal
        self.dict[leechTag] = float(self.dict[leechTag]) + leechVal

    def resourceStarter(self, leechVal, leechTag):
        self.dict[leechTag] += leechVal

    def showDict(self):
        for x in self.dict:
            print("%s : %f" % (x, self.dict[x]))

    def returnDict(self):
        return self.dict

    def returnLabels(self):
        labels = []
        for x in self.dict:
            labels.append(x)
   #     labels.pop(0)
        return labels

    def returnValues(self):
        values = []
        for x in self.dict:
            values.append(self.dict[x])
    #    values.pop(0)
        return values

    def returnExplode(self):
        explode = []
        for x in self.dict:
            explode.append(0)
        explode.pop(0)
        explode[0] = 0.1
        return explode
