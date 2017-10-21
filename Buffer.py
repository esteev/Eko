
class Buffer:

    buffer = None

    def __init__(self, sizeX, sizeY, sizeZ):
    #def __init__(self, depth):
        self.buffer = [[[0 for col in range(sizeX)] for row in range(sizeY)] for x in range(sizeZ)]
    #    self.buffer = [0 for col in range(depth)]

    def printer(self):
        for x in range(len(self.buffer)):
            print self.buffer[x]

    def returnPos(self, i, j, k):
        return self.buffer[i][j][k]

    def updatePos(self, i, j, k, ch):
        self.buffer[i][j][k] = ch

