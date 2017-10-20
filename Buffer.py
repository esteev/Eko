
class Buffer:

    buffer = None

    def __init__(self, sizeX, sizeY, sizeZ):
        self.buffer = [[[0 for col in range(sizeX)] for row in range(sizeY)] for x in range(sizeZ)]

    def printer(self):
        for x in range(len(self.buffer)):
            print self.buffer[x]
