from psonic import Message
from time import sleep

# Initial:
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

# Add BPM support:
class Metronome:
    TICKS_PER_BEAT = 4
    BEATS_PER_BAR = 4

    def __init__(self, bpm=120):
        self.bpm = bpm

        self.signal = Message()

        self.tick_number = 0
        self.beat_number = 0
        self.bar_number = 0

    def wait_for_tick(self):
        self.signal.sync()

    def cue(self):
        if self.is_active:
            self.signal.cue()

    def tick(self):
        if self.is_active:
            self.tick_number = self.tick_number + 1

            if self.is_new_beat:
                self.beat_number = self.beat_number + 1

            if self.is_new_bar:
                self.bar_number = self.bar_number + 1

    def tick_sleep(self):
        beats_per_sec = float(self.bpm / 60)
        tick_len = 1 / (self.TICKS_PER_BEAT * beats_per_sec)
        sleep(tick_len)

# Add beat and bar support:
    def bar_sleep(self, wait_len):
        for _ in range(int(wait_len * self.BEATS_PER_BAR * self.TICKS_PER_BEAT)):
            self.wait_for_tick()

    def beat_sleep(self, wait_len):
        for _ in range(int(wait_len * self.TICKS_PER_BEAT)):
            self.wait_for_tick()
