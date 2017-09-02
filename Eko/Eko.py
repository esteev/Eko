from Core import *
#import Core as core
import Abiotics as Abiotics


class Eko(Core,object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = phosphorousCycle = sulphurCycle = None

    def init(self):
        super(Eko, self).init()
        print("1")
        self.nitrogenCycle = Abiotics.Nitrogen()
        self.pond()

    def update(self, timePassed):
        self.gameTime += timePassed
        print(self.gameTime)

    def stop(self):
        Core._exit = True

    def pond(self):
        print (self.nitrogenCycle.nitrogenTake(10, "air"))



eko = Eko()
eko.run()
