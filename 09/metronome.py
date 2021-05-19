from psonic import Message
from time import sleep


class Metronome:
    def __init__(self, bpm=120, ticks_per_beat=4, beats_per_bar=4):
        self.bpm = bpm
        self.ticks_per_beat = ticks_per_beat
        self.beats_per_bar = beats_per_bar
        self.tick_to_stop_at = None
        self.signal = Message()
        self.tick_number = 0
        self.beat_number = 0
        self.bar_number = 0

    @property
    def tick_tuple(self):
        return (
            self.bar_number,
            self.relative_beat_number,
            self.relative_tick_number,
        )

    @property
    def relative_beat_number(self):
        return ((self.beat_number - 1) % self.beats_per_bar) + 1

    @property
    def relative_tick_number(self):
        return ((self.tick_number - 1) % self.ticks_per_beat) + 1    

    def wait_for_tick(self):
        self.signal.sync()

    def cue(self):
        if self.is_active:
            self.signal.cue()

    @property
    def is_new_beat(self):
        return self.tick_number % self.ticks_per_beat == 1

    @property
    def is_new_bar(self):
        return self.is_new_beat and self.beat_number % self.beats_per_bar == 1

    def tick(self):
        if self.is_active:
            self.tick_number = self.tick_number + 1

            if self.is_new_beat:
                self.beat_number = self.beat_number + 1

            if self.is_new_bar:
                self.bar_number = self.bar_number + 1

    def tick_sleep(self):
        beats_per_sec = float(self.bpm / 60)
        tick_len = 1 / (self.ticks_per_beat * beats_per_sec)
        sleep(tick_len)

    @property
    def is_active(self):
        return self.tick_to_stop_at is None or self.tick_number < self.tick_to_stop_at

    def bar_sleep(self, wait_len):
        for _ in range(int(wait_len * self.beats_per_bar * self.ticks_per_beat)):
            self.wait_for_tick()

    def beat_sleep(self, wait_len):
        for _ in range(int(wait_len * self.ticks_per_beat)):
            self.wait_for_tick()

    def stop_at(self, total_ticks):
        self.tick_to_stop_at = total_ticks
