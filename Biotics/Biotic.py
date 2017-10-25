from enum import Enum


class Jansankhya:

    algae = catTail = zooPlankton = tadpole = greenSunFish = largeBassMouth = stork = []

    def __init__(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.populator(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount)

    def populator(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.algae = [Algae() for i in range(algaeCount)]
        self.looper(self.algae, algaeCount, al)
        self.looper(self.catTail, catTailCount, ct)
        self.looper(self.zooPlankton, zooPlanktonCount, zp)
        self.looper(self.tadpole, tadpoleCount, tp)
        self.looper(self.greenSunFish, smallFishyCount, gr)
        self.looper(self.largeBassMouth, bigFishyCount, lb)
        self.looper(self.stork, storkCount, st)

    def looper(self, list, listCount, listEle):
        for i in range(listCount):
            list.append(listEle)

    def popShow(self):
        print("Algae :" + len(self.algae))


class Drives(Enum):
    PAIN = 0
    DANGER = 1
    HUNGER = 2
    LIBIDO = 4
    FREE = 8


class Actions(Enum):
    RUN = 0
    EAT = 1
    REPRODUCE = 2
    FREE = 4


class Biotic:

    id = health = sexualMaturity = foodChainRank = lifeExpectancy = None
    waterConcentration = None
    currentState = None

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        self.id = id
        self.health = health
        self.sexualMaturity = sexualMaturity
        self.waterConcentration = waterConcentration
        self.foodChainRank = foodChainRank
        self.lifeExpectancy = lifeExpectancy

    def returnId(self):
        return self.id

    def returnFoodChainRank(self):
        return  self.foodChainRank

    def returnMaturity(self):
        return  self.sexualMaturity

# Layer 0 of the food chain

class Algae(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(Algae, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)


class CatTail(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(CatTail, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)


# Layer 1 of the food chain


class ZooPlankton(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(ZooPlankton, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)


class Tadpole(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(Tadpole, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)

# Layer 2 of the food chain


class GreenSunfish(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(GreenSunfish, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)

# Layer 3 of the food chain


class LargeBassMouth(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(LargeBassMouth, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)

#Layer 4 of the food chain


class Stork(Biotic, object):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy):
        super(Stork, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank, lifeExpectancy)

'''
layer 0
algae
cattail

layer 1
tadpole
zooplankton

layer 2
small fishy

layer 3
big fishy

layer 4
stork
'''