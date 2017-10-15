import threading
import time


class Sun(threading.Thread):

    intensityVal = None

    def __init__(self, val):
        threading.Thread.__init__(self)
        self.intensityVal = val


class Atmosphere(threading.Thread):

    oxygenVal = nitrogenVal = humidVal = None

    def __init__(self, val):
        threading.Thread.__init__(self)
        self.humidVal = val


class Forecast:

    heat = moisture = None

    def __init__(self):
        self.heat = Sun(1)
        self.moisture = Atmosphere(1)

    def update(self):
        self.recaliberateSun()
        self.recaliberateHumidity()

    # Values are static for     Now

    def recaliberateSun(self):
        self.heat.intensityVal = 1

    def recaliberateHumidity(self):
        self.moisture.humidVal = 1

    def getHeat(self):
        return self.heat.intensityVal

    def getMoisture(self):
        return self.moisture.humidVal
