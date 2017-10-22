from enum import Enum


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

    # def return

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