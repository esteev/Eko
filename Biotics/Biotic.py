from enum import IntEnum
import random
import math


class Jansankhya:

    algae = catTail = zooPlankton = tadpole = greenSunFish = largeBassMouth = stork = []
    organismList = []

    def __init__(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.populator(algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount)

    def populator(self, algaeCount, catTailCount, zooPlanktonCount, tadpoleCount, smallFishyCount, bigFishyCount, storkCount):
        self.algae = [Algae("al", 1, 1, 0, 5, 0.5) for i in range(algaeCount)]
        self.catTail = [CatTail("ct", 2, 1, 0, 5, 1) for i in range(catTailCount)]
        self.zooPlankton = [ZooPlankton("zp", 1, 1, 1, 5, 1.5) for i in range(zooPlanktonCount)]
        self.tadpole = [Tadpole("tp", 3, 2, 2, 5, 2) for i in range(tadpoleCount)]
        self.greenSunFish = [GreenSunfish("gs", 10, 5, 3, 5, 2.5) for i in range(smallFishyCount)]
        self.largeBassMouth = [LargeBassMouth("lb", 15, 7, 4, 5, 3) for i in range(bigFishyCount)]
        self.stork = [Stork("st", 30, 10, 5, 5, 3.5) for i in range(storkCount)]
        self.addToList()

    def organismListUpdater(self):
        newAlgae = []
        newCatTail = []
        newZooPlank = []
        newTadpole = []
        newSmallFishy = []
        newBigFishy = []
        newStork = []
        for x in self.organismList:
            if x.getId() == "al":
                newAlgae.append(x)
            elif x.getId() == "ct":
                newCatTail.append(x)
            elif x.getId() == "zp":
                newZooPlank.append(x)
            elif x.getId() == "tp":
                newTadpole.append(x)
            elif x.getId() == "gs":
                newSmallFishy.append(x)
            elif x.getId() == "lb":
                newBigFishy.append(x)
            elif x.getId() == "st":
                newStork.append(x)
     #   print (newAlgae)

        self.algae = newAlgae
        self.catTail = newCatTail
        self.zooPlankton = newZooPlank
        self.tadpole = newTadpole
        self.greenSunFish = newSmallFishy
        self.largeBassMouth = newBigFishy
        self.stork = newStork


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

    def popPrintDetailed(self):
        print(self.organismList)

    def organismListShuffler(self):
        random.shuffle(self.organismList)


class Drives(IntEnum):
    PAIN = 1
    DANGER = 2
    LIBIDO = 3
    FREE = 4

class Actions(IntEnum):
    RUN = 1
    REPRODUCE = 2
    FREE = 3


class Biotic:

    id = health = sexualMaturity = foodChainRank = lifeExpectancy = hungerTolerance = None
    initialState = currentState = None
    currentHunger = khanaHaiKya = maxHealth = 0

    def __init__(self, id, health, sexualMaturity, foodChainRank, lifeExpectancy, hungerTolerance):
        self.id = id
        self.health = health
        self.maxHealth = health
        self.sexualMaturity = sexualMaturity
        self.foodChainRank = foodChainRank
        self.lifeExpectancy = lifeExpectancy
        self.hungerTolerance = hungerTolerance
        self.currentState = self.randomStateProvider()

    def randomStateProvider(self):
        return 2 ** random.randint(0, Drives.FREE+1)

    def update(self, timePassed, khanaHaiKya):
        self.khanaHaiKya = khanaHaiKya
        self.priorityBasedActions()

        self.hungerIncrement(timePassed)

        maxVal = 2 ** Drives.FREE - 1
        self.currentState = random.randint(0, maxVal)


    def hungerIncrement(self, timePassed):
        if(timePassed == 0):
            timePassed = 2
        self.currentHunger += math.log( int(timePassed), 10)

    def priorityBasedActions(self):
        priority = self.beingScheduler()

        if priority == Drives.PAIN:
            self.pain()
        elif priority == Drives.DANGER:
            self.danger()
        elif self.currentHunger >= self.hungerTolerance:
            self.hunger()
        elif priority == Drives.LIBIDO:
            self.libido()
        elif priority == Drives.FREE:
            self.free()

    def pain(self):
      #  pass
         print("PAIN")
#        self.hungerIncrement(2)

    def danger(self):
      #  pass
        print("DANGER")

    def hunger(self):
        print("HUNGER")
        if(self.khanaHaiKya == 1):
            self.currentHunger = 0
            print ("Khaaayyaaaa ")
        else:
            print("Bhookaaaaaaa " + str(self.__class__.__name__))
            self.health -= self.maxHealth

    def libido(self):
      #  pass
        print("LIBIDO")

    def free(self):
  #      pass
        print("FREE")

    def beingScheduler(self):
        temp = self.currentState
        if temp & 1 << Drives.PAIN - 1 == 1 << Drives.PAIN - 1:
            return Drives.PAIN

        if temp & 1 << Drives.DANGER - 1 == 1 << Drives.DANGER - 1:
            return Drives.DANGER

        if temp & 1 << Drives.LIBIDO - 1 == 1 << Drives.LIBIDO - 1:
            return Drives.LIBIDO

        return Drives.FREE

    def getId(self):
        return self.id

    def getFoodChainRank(self):
        return self.foodChainRank

    def getMaturity(self):
        return  self.sexualMaturity

# Layer 0 of the food chain


class Algae(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(Algae, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance)

    def hunger(self):
        self.currentHunger = 0
        print ("Khaaayyaaaa ")

class CatTail(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(CatTail, self).__init__(id, health, sexualMaturity, foodChainRank, lifeExpectancy, hungerTolerance)


# Layer 1 of the food chain


class ZooPlankton(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(ZooPlankton, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance)


class Tadpole(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(Tadpole, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance)

# Layer 2 of the food chain


class GreenSunfish(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(GreenSunfish, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance)

# Layer 3 of the food chain


class LargeBassMouth(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(LargeBassMouth, self).__init__(id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance)

#Layer 4 of the food chain


class Stork(Biotic, object):

    def __init__(self, id, health, sexualMaturity,  foodChainRank, lifeExpectancy, hungerTolerance):
        super(Stork, self).__init__(id, health, sexualMaturity, foodChainRank, lifeExpectancy, hungerTolerance)

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

