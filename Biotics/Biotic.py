from enum import Enum


class Jansankhya:

    algae = catTail = zooPlankton = tadpole = greenSunFish = largeBassMouth = stork = []

    def __init__(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.populator(algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount)

    def populator(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.algae = [Algae("1", 1, 1, 0.01, 0, 5) for i in range(algaeCount)]
        self.catTail = [CatTail("2", 2, 1, 0.1, 0, 5) for i in range(catTailCount)]
        self.zooPlankton = [ZooPlankton("3", 1, 1, 0.01, 1, 5) for i in range(zooPlanktonCount)]
        self.tadpole = [Tadpole("4", 3, 2, 0.2, 1.5, 5) for i in range(tadpoleCount)]
        self.greenSunFish = [GreenSunfish("5", 10, 5, 0.7, 2, 5) for i in range(smallFishyCount)]
        self.largeBassMouth = [LargeBassMouth("6", 15, 7, 1, 3, 5) for i in range(bigFishyCount)]
        self.stork = [Stork("7", 30, 10, 1.2, 4, 5) for i in range(storkCount)]
        self.printer()
        self.totalPopPrint()

    def printer(self):
        print ('Algae = '+str(len(self.algae)))
        print ('CatTail = '+str(len(self.catTail)))
        print ('Zoo Plankton = '+str(len(self.zooPlankton)))
        print ('Tadpoles = '+str(len(self.tadpole)))
        print ('Green Sunfish = ' + str(len(self.greenSunFish)))
        print ('LargeBassMouth = '+str(len(self.largeBassMouth)))
        print ('Stork = '+str(len(self.stork)))

    def totalPopPrint(self):
        print("Total Population = " + str(len(self.algae)+len(self.catTail)+len(self.zooPlankton)+len(self.tadpole)+len(self.greenSunFish)+len(self.largeBassMouth)+len(self.stork)))



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

drives = Drives()
actions = Actions()

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

    def update(self):
        self.priorityBasedActions()

    def priorityBasedActions(self):
        priority = self.beingScheduler()

        if priority == drives.pain:
            print("pain")
        elif priority == drives.danger:
            print("danger")
        elif priority == drives.hunger:
            print("hunger")
        elif priority == drives.libido:
            print("libido")
        elif priority == drives.free:
            print("free")

    def beingScheduler(self):
            if self.currentState & 1 << drives.pain == 1 << drives.pain:
                return drives.pain

            if self.currentState & 1 << drives.danger == 1 << drives.danger:
                return drives.danger

            if self.currentState & 1 << drives.hunger == 1 << drives.hunger:
                return drives.hunger

            if self.currentState & 1 << drives.libido == 1 << drives.libido:
                return drives.libido

            return drives.free

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