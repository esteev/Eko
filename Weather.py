
class Sun:

    intensityVal = None

    def __init__(self, val):
        self.intensityVal = val


class Humidity:

    humidVal = None

    def __init__(self, val):
        self.humidVal = val


class Forecast:

    heat = moisture = None

    def __init__(self):
        self.heat = Sun(10)
        self.moisture = Humidity(10)

    def change(self):
        self.recaliberateSun()
        self.recaliberateHumidity()

    def recaliberateSun(self):
        self.heat.intensityVal = 10

    def recaliberateHumidity(self):
        self.moisture.humidVal = 10