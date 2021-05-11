from .singleton import Singleton

from psonic import Message, sleep
from math import ceil


class Metronome(metaclass=Singleton):
    def __init__(self, bpm, ticks_per_beat=4, beats_per_bar=4):
        self.bpm = bpm
        self.ticks_per_beat = ticks_per_beat
        self.beats_per_bar = beats_per_bar
        self.signal = Message()
        self.tick_number = 0
        self.beat_number = 0
        self.bar_number = 0

    def wait_for_beats(self, beats_to_wait):
        self.wait_for_ticks(beats_to_wait * self.ticks_per_beat)

    def wait_for_ticks(self, ticks_to_wait):
        for _ in range(ticks_to_wait):
            self.wait_for_tick()

    def wait_for_tick(self):
        self.signal.sync()

    def cue(self):
        self.signal.cue()

    @property
    def is_new_beat(self):
        return self.tick_number % self.ticks_per_beat == 1

    @property
    def is_new_bar(self):
        return self.is_new_beat and self.beat_number % self.beats_per_bar == 1

    def tick(self):
        self.tick_number = self.tick_number + 1

        if self.is_new_beat:
            self.beat_number = self.beat_number + 1

        if self.is_new_bar:
            self.bar_number = self.bar_number + 1

    def tick_sleep(self):
        beats_per_sec = float(self.bpm / 60)
        tick_len = 1 / (self.ticks_per_beat * beats_per_sec)
        sleep(tick_len)

    def tick_forever(self):
        while True:
            self.tick()
            self.cue()
            self.tick_sleep()

    def beat_sleep(self, wait_len):
        for _ in range(int(wait_len * self.ticks_per_beat)):
            self.wait_for_tick()
