#nitrogen
#water
#carbon
#phosphorous
#sulphur
#oxygen


class Resource:

    dict = {}

    def __init__(self, dictTemp):
        self.dict = dictTemp

    def resourceLeech(self, leechVal, leechTag, seedTag):
        self.dict[seedTag] -= leechVal
        self.dict[leechTag] += leechVal

    def showDict(self):
        for x in self.dict:
            print("%s : %f" % (x, self.dict[x]))

