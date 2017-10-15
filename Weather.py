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
    humidTolerance = 20

    def __init__(self):
        self.heat = Sun(1)
        self.moisture = Atmosphere(1)

    def update(self):
        self.recaliberateSun()

    def changeHumidity(self, val):
        self.moisture.humidVal += val

    def recaliberateSun(self):
        #Sun is static
        self.heat.intensityVal = 1

    def getHeat(self):
        return self.heat.intensityVal

    def getMoisture(self):
        return self.moisture.humidVal

