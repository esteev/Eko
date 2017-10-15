#nitrogen
#water
#carbon
#phosphorous
#sulphur
#oxygen

from Resource import *


class WaterCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'Biosphere': 0}
        super(WaterCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(80, 'Hydrosphere', 'unUsed')
        self.resourceLeech(10, 'Biosphere', 'unUsed')

    def waterEvaporate(self, waterLeechVal):
        self.resourceLeech(waterLeechVal, 'Hydrosphere', 'Atmosphere')

    def waterPrecipitate(self, waterLeechVal):
        self.resourceLeech(waterLeechVal, 'Atmosphere', 'Hydrosphere')

    def waterConsume(self, waterLeechVal):
        self.resourceLeech((waterLeechVal, 'Hydrosphere', 'Biosphere'))

    def waterRelease(self, waterLeechVal):
        self.resourceLeech((waterLeechVal, 'Biosphere', 'Hydrosphere'))


class NitrogenCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'NH3': 0, 'NO3-': 0}
        super(NitrogenCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(50, 'Hydrosphere', 'unUsed')
        self.resourceLeech(20, 'NH3', 'unUsed')
        self.resourceLeech(20, 'NO3-', 'unUsed')

    def nitrogenEvaporate(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, 'Hydrosphere', 'Atmosphere')

    def nitrogenPrecipitate(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, 'Atmosphere', 'Hydrosphere')

    def denitrification(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, 'NO3-', 'Hydrosphere')

    def nitrification(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, 'NH3', 'NO3-')

    def nitrogenFixation(self, nitrogenLeechVal):
        self.resourceLeech(nitrogenLeechVal, 'Hydrosphere', 'NH3')


class CarbonCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'H2CO3': 0, 'HCO3-': 0, 'CO32-': 0}
        super(CarbonCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(40, 'Hydrosphere', 'unUsed')
        self.resourceLeech(20, 'H2CO3', 'unUsed')
        self.resourceLeech(20, 'HCO3-', 'unUsed')
        self.resourceLeech(10, 'CO32-', 'unUsed')

    def carbonEvaporate(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'Hydrosphere', 'Atmosphere')

    def carbonPrecipitate(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'Atmosphere', 'Hydrosphere')

    def carbonicAcid(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'Hydrosphere', 'H2C03')

    def firstIonization(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'H2CO3', 'HCO3-')

    def secondIonization(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'Hydrosphere', 'H2C03')
