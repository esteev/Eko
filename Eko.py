from Core import *
#import Core as core
import Abiotics as Abiotics


class Eko(Core,object):
    gameTime = 0.0
    nitrogenCycle = waterCycle = carbonCycle = phosphorousCycle = sulphurCycle = None

    def init(self):
        super(Eko, self).init()
      #  print("1")
        dictTemp = {}
        dictTemp["unUsed"] = 100
        self.nitrogenCycle = Abiotics.Resource(dictTemp)
        self.pond()

    def update(self, timePassed):
        self.gameTime += timePassed
     #W   print(self.gameTime)

    def stop(self):
        Core._exit = True

    def pond(self):
        self.nitrogenCycle.showDict()
        #print(self.nitrogenCycle.dict)


eko = Eko()
eko.run()
