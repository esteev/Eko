
class Biotic:

    id = health = sexualMaturity = None
    waterConcentration = None

    def __init__(self, id, health, sexualMaturity):
        self.id = id
        self.health = health
        self.sexualMaturity = sexualMaturity


class Algae(object, Biotic):

    def __init__(self, id, health, sexualMaturity, waterConcentration):
        super(Algae, self).__init__(id, health, sexualMaturity)

