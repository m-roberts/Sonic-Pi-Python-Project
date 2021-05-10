from .singleton import Singleton
from psonic import Message
from math import ceil

class Metronome(metaclass=Singleton):
    def __init__(self, bpm, ticks_per_beat=4):
        self.bpm = bpm
        self.ticks_per_beat = ticks_per_beat
        self.signal = Message()
        self.tick_number = 0

    def wait_for_beats(self, beats_to_wait):
        self.wait_for_ticks(beats_to_wait * self.ticks_per_beat)

    def wait_for_ticks(self, ticks_to_wait):
        for _ in range(ticks_to_wait):
            self.wait_for_tick()

    def wait_for_tick(self):
        self.signal.sync()

    def tick(self):
        self.tick_number = self.tick_number + 1
        self.signal.cue()

    def tick_forever(self):
        beats_per_sec = float(BPM / 60)
        tick_len = 1 / (self.ticks_per_beat * beats_per_sec)

        while True:
            self.tick()
            sleep(tick_len)
