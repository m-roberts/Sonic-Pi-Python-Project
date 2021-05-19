from psonic import Message
from time import sleep

class Metronome():
    def __init__(self):
        self.signal = Message()

    def wait_for_tick(self):
        self.signal.sync()

    def cue(self):
        if self.is_active:
            self.signal.cue()

    def tick_sleep(self):
        sleep(0.5)
