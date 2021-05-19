from threading import Thread

# Initial state
class LoopingTrack:
    def __init__(self, func=None):
        self.enabled = False
        self.func = func

        self._thread = Thread(target=self.call_function_forever)
        self._thread.start()



# v1 change: user adds function to loop forever
class LoopingTrack:
    def __init__(self, func=None):
        self.enabled = False
        self.func = func

        self._thread = Thread(target=self.call_function_forever)
        self._thread.start()

    def call_function_forever(self):
        while self.enabled:
            self.func()

# v2 change: waits for metronome
class LoopingTrack:
    def __init__(self, metronome, func=None):
        self.enabled = False
        self.metronome = metronome
        self.func = func

        self._thread = Thread(target=self.call_function_forever)
        self._thread.start()

    def call_function_forever(self):
        while self.enabled:
            self.metronome.wait_for_tick()
            self.func()
