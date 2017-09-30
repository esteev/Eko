#nitrogen
#water
#carbon
#phosphorous
#sulphur
#oxygen

from Resource import *


class WaterCycle(Resource, object):

    def __init__(self, dictTemp):
        super(WaterCycle, self).__init__(dictTemp)
        self.addTag("Atmosphere")
        self.addTag("Pond")
        self.addTag("Biotic")
        self.resourceLeech(10, "Atmosphere", "unUsed")
        self.resourceLeech(80, "Pond", "unUsed")
        self.resourceLeech(10, "Biotic", "unUsed")

    def waterEvaporate(self, waterLeechVal):
        self.resourceLeech(waterLeechVal, "Pond", "Atmosphere")

    def waterPrecipitate(self, waterLeechVal):
        self.resourceLeech(waterLeechVal, "Atmosphere", "Pond")

    def waterConsume(self, waterLeechVal):
        self.resourceLeech((waterLeechVal, "Pond", "Biotic"))

    def waterRelease(self, waterLeechVal):
        self.resourceLeech((waterLeechVal, "Biotic", "Pond"))


class NitrogenCycle(Resource, object):

    def __init__(self, dictTemp):
        super(NitrogenCycle, self).__init__(dictTemp)
        self.addTag("Atmospheric N2")
        self.addTag("Dissolved N2")
        self.addTag("NH3")
        self.addTag("NO3-")
        self.resourceLeech(10, "Atmospheric N2", "unUsed")
        self.resourceLeech(50, "Dissolved N2", "unUsed")
        self.resourceLeech(20, "NH3", "unUsed")
        self.resourceLeech(20, "NO3-", "unUsed")

    def nitrogenEvaporate(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, "Dissolved N2", "Atmospheric N2")

    def nitrogenPrecipitate(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, "Atmospheric N2", "Dissolved N2")

    def denitrification(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, "NO3-", "Dissolved N2")

    def nitrification(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, "NH3", "NO3-")

    def nitrogenFixation(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, "Dissolved N2", "NH3")


class CarbonCycle(Resource, object):

    def __init__(self, dictTemp):
        super(CarbonCycle,self).__init__(dictTemp)
        self.addTag("Dissolved CO2")
        self.addTag("Atmospheric CO2")
        self.addTag("H2CO3")
        self.addTag("HCO3-")
        self.addTag("CO32-")
        self.resourceLeech(10, "Atmospheric CO2", "unUsed")
        self.resourceLeech(40, "Dissolved CO2", "unUsed")
        self.resourceLeech(20, "H2CO3", "unUsed")
        self.resourceLeech(20, "HCO3-", "unUsed")
        self.resourceLeech(10, "CO32-", "unUsed")

    def carbonEvaporate(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, "Dissolved CO2", "Atmospheric CO2")

    def carbonPrecipitate(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, "Atmospheric CO2", "Dissolved CO2")

    def carbonicAcid(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, "Dissolved CO2", "H2C03")

    def firstIonization(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, "H2CO3", "HCO3-")

    def secondIonization(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, "Dissolved CO2", "H2C03")
