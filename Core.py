import time


class Core:

    _running = True
    _exit = False
    _startTime = _timePassed = _cumTime = 0.0
    _breakInterval = 2.0

    def stop(self):
        pass

    def run(self):
        self.init()
        self.gameLoop()

    def init(self):
        self._running = True
      #  print("2")

    def gameLoop(self):
        _startTime = time.time()
        _cumTime = _startTime

        while self._running:
            _timePassed = time.time() - _cumTime
            _cumTime += _timePassed
            self.update(_timePassed)
            time.sleep(self._breakInterval)

    def update(self, timePassed):
        pass

    def draw(self):
        pass

