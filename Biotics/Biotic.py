from enum import IntEnum


class Jansankhya:

    algae = catTail = zooPlankton = tadpole = greenSunFish = largeBassMouth = stork = []
    organismList = []

    def __init__(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.populator(algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount)

    def populator(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.algae = [Algae("1", 1, 1, 0, 5) for i in range(algaeCount)]
        self.catTail = [CatTail("2", 2, 1, 0, 5) for i in range(catTailCount)]
        self.zooPlankton = [ZooPlankton("3", 1, 1, 1, 5) for i in range(zooPlanktonCount)]
        self.tadpole = [Tadpole("4", 3, 2, 1.5, 5) for i in range(tadpoleCount)]
        self.greenSunFish = [GreenSunfish("5", 10, 5, 2, 5) for i in range(smallFishyCount)]
        self.largeBassMouth = [LargeBassMouth("6", 15, 7, 3, 5) for i in range(bigFishyCount)]
        self.stork = [Stork("7", 30, 10, 4, 5) for i in range(storkCount)]
        self.addToList()
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

    def addToList(self):
        for x in self.algae:
            self.organismList.append(x)

        for x in self.catTail:
            self.organismList.append(x)

        for x in self.zooPlankton:
            self.organismList.append(x)

        for x in self.tadpole:
            self.organismList.append(x)

        for x in self.greenSunFish:
            self.organismList.append(x)

        for x in self.largeBassMouth:
            self.organismList.append(x)

        for x in self.stork:
            self.organismList.append(x)

    def totalPopPrint(self):
        print("Total Population = " + str(len(self.organismList)))


class Drives(IntEnum):
    PAIN = 1
    DANGER = 2
    HUNGER = 3
    LIBIDO = 4
    FREE = 5


class Actions(IntEnum):
    RUN = 1
    EAT = 2
    REPRODUCE = 4
    FREE = 8


class Biotic:

    id = health = sexualMaturity = foodChainRank = lifeExpectancy = None
    currentState = None

    def __init__(self, id, health, sexualMaturity, foodChainRank, lifeExpectancy):
        self.id = id
        self.health = health
        self.sexualMaturity = sexualMaturity
        self.foodChainRank = foodChainRank
        self.lifeExpectancy = lifeExpectancy
        self.currentState = 0

    def update(self):
        self.priorityBasedActions()

    def priorityBasedActions(self):
        priority = self.beingScheduler()

        if priority == Drives.PAIN:
            print("PAIN")
        elif priority == Drives.DANGER:
            print("DANGER")
        elif priority == Drives.HUNGER:
            print("HUNGER")
        elif priority == Drives.LIBIDO:
            print("LIBIDO")
        elif priority == Drives.FREE:
            print("FREE")

    def beingScheduler(self):
        temp = self.currentState
        if temp & 1 << Drives.PAIN - 1 == 1 << Drives.PAIN - 1:
            return Drives.PAIN

        if temp & 1 << Drives.DANGER - 1 == 1 << Drives.DANGER - 1:
            return Drives.DANGER

        if temp & 1 << Drives.HUNGER - 1 == 1 << Drives.HUNGER - 1:
            return Drives.HUNGER

        if temp & 1 << Drives.LIBIDO - 1 == 1 << Drives.LIBIDO - 1:
            return Drives.LIBIDO

        return Drives.FREE

    def returnId(self):
        return self.id

    def returnFoodChainRank(self):
        return  self.foodChainRank

    def returnMaturity(self):
        return  self.sexualMaturity

# Layer 0 of the food chain

class Algae(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(Algae, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy)


class CatTail(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(CatTail, self).__init__(id, health, sexualMaturity, foodChainRank, lifeExpectancy)


# Layer 1 of the food chain


class ZooPlankton(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(ZooPlankton, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy)


class Tadpole(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(Tadpole, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy)

# Layer 2 of the food chain


class GreenSunfish(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(GreenSunfish, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy)

# Layer 3 of the food chain


class LargeBassMouth(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(LargeBassMouth, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy)

#Layer 4 of the food chain


class Stork(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy):
        super(Stork, self).__init__(id, health, sexualMaturity, foodChainRank, lifeExpectancy)

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

