
class Biotic:

    id = health = sexualMaturity = foodChainRank = None
    waterConcentration = None

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        self.id = id
        self.health = health
        self.sexualMaturity = sexualMaturity
        self.waterConcentration = waterConcentration
        self.foodChainRank = foodChainRank


# Layer 0 of the food chain

class Algae(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(Algae, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)


class CatTail(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(CatTail, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)


# Layer 1 of the food chain


class ZooPlankton(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(ZooPlankton, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)


class Tadpole(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(Tadpole, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)

# Layer 2 of the food chain


class GreenSunfish(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(GreenSunfish, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)

# Layer 3 of the food chain


class LargeBassMouth(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(LargeBassMouth, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)

#Layer 4 of the food chain


class Stork(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration, foodChainRank):
        super(Stork, self).__init__(id, health, sexualMaturity, waterConcentration, foodChainRank)

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