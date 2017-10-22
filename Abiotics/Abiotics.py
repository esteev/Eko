#nitrogen
#water
#carbon
#oxygen
#phosphorous
#sulphur


from Resource import *


class WaterCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'Biosphere': 0}
        super(WaterCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(80, 'Hydrosphere', 'unUsed')
        self.resourceLeech(10, 'Biosphere', 'unUsed')

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

    def carbonicAcid(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'Hydrosphere', 'H2C03')

    def firstIonization(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'H2CO3', 'HCO3-')

    def secondIonization(self, carbonLeechVal):
        self.resourceLeech(carbonLeechVal, 'Hydrosphere', 'H2C03')


class OxygenCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'Sleh': 0, 'Slah': 0, 'Slooh': 0}
        super(OxygenCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(40, 'Hydrosphere', 'unUsed')
        self.resourceLeech(20, 'Sleh', 'unUsed')
        self.resourceLeech(20, 'Slah', 'unUsed')
        self.resourceLeech(10, 'Slooh', 'unUsed')


class PhosphorousCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'Bleh': 0, 'Blooh': 0, 'Blaah': 0}
        super(PhosphorousCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(40, 'Hydrosphere', 'unUsed')
        self.resourceLeech(20, 'Bleh', 'unUsed')
        self.resourceLeech(20, 'Blooh', 'unUsed')
        self.resourceLeech(10, 'Blaah', 'unUsed')


class SulphurCycle(Resource, object):

    def __init__(self):
        dictTemp = {'unUsed': 100, 'Atmosphere': 0, 'Hydrosphere': 0, 'Cleh': 0, 'Clooh': 0, 'Claah': 0}
        super(SulphurCycle, self).__init__(dictTemp)
        self.resourceLeech(10, 'Atmosphere', 'unUsed')
        self.resourceLeech(40, 'Hydrosphere', 'unUsed')
        self.resourceLeech(20, 'Cleh', 'unUsed')
        self.resourceLeech(20, 'Clooh', 'unUsed')
        self.resourceLeech(10, 'Claah', 'unUsed')


