#nitrogen
#water
#carbon
#phosphorous
#sulphur
#oxygen


class Nitrogen:

    nitrogen = 100.0
    dict = {}

    def __init__(self):
        self.nitrogen = 100.0

    def nitrogenTake(self, param, tag):
        self.nitrogen -= param
        if tag in self.dict:
            self.dict[tag] = self.dict[tag]+1
        else:
            self.dict[tag] = 1
        return param

    def nitrogenReturn(self, param, tag):
        self.nitrogen += param
        if self.dict[tag]-1 >= 0:
            self.dict[tag] = self.dict[tag] - 1
        else:
            self.dict.pop(tag, None)


class Water:

    water = 100.0
    dict = {}

    def __init__(self):
        self.water = 100.0

    def waterTake(self, param, tag):
        self.water -= param
        if tag in self.dict:
            self.dict[tag] = self.dict[tag]+1
        else:
            self.dict[tag] = 1

    def waterReturn(self, param, tag):
        self.water += param
        if self.dict[tag]-1 >= 0:
            self.dict[tag] = self.dict[tag] - 1
        else:
            self.dict.pop(tag, None)


class Carbon:

    carbon = 100.0
    dict = {}

    def __init__(self):
        self.carbon = 100.0

    def carbonTake(self, param, tag):
        self.carbon -= param
        if tag in self.dict:
            self.dict[tag] = self.dict[tag]+1
        else:
            self.dict[tag] = 1

    def carbonReturn(self, param, tag):
        self.carbon += param
        if self.dict[tag]-1 >= 0:
            self.dict[tag] = self.dict[tag] - 1
        else:
            self.dict.pop(tag, None)


class Phosphorous:

    phosphorous = 100.0
    dict = {}

    def __init__(self):
        self.phosphorous = 100.0

    def phosphorousTake(self, param, tag):
        self.phosphorous -= param
        if tag in self.dict:
            self.dict[tag] = self.dict[tag]+1
        else:
            self.dict[tag] = 1

    def phosphorousReturn(self, param, tag):
        self.phosphorous += param
        if self.dict[tag]-1 >= 0:
            self.dict[tag] = self.dict[tag] - 1
        else:
            self.dict.pop(tag, None)


class Sulphur:

    sulphur = 100.0
    dict = {}

    def __init__(self):
        self.suphur = 100.0

    def sulphurTake(self, param, tag):
        self.sulphur -= param
        if tag in self.dict:
            self.dict[tag] = self.dict[tag]+1
        else:
            self.dict[tag] = 1

    def sulphurReturn(self, param, tag):
        self.sulphur += param
        if self.dict[tag]-1 >= 0:
            self.dict[tag] = self.dict[tag] - 1
        else:
            self.dict.pop(tag, None)


class Oxygen:

    oxygen = 100.0
    dict = {}

    def __init__(self):
        self.oxygen = 100.0

    def oxygenTake(self, param, tag):
        self.oxygen -= param
        if tag in self.dict:
            self.dict[tag] = self.dict[tag]+1
        else:
            self.dict[tag] = 1

    def oxygenReturn(self, param, tag):
        self.oxygen += param
        if self.dict[tag]-1 >= 0:
            self.dict[tag] = self.dict[tag] - 1
        else:
            self.dict.pop(tag, None)
