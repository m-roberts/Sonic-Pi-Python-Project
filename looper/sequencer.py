from .metronome import Metronome
from .track import Track


class Sequencer:
    def __init__(self, bpm=120, ticks_per_beat=4):
        Metronome(bpm, ticks_per_beat)

        self.kick = Track("kick")
        self.snare = Track("snare")
        self.perc = Track("perc")
        self.sample = Track("sample")
        self.bass = Track("bass")
        self.lead = Track("lead")
        self.arp = Track("arp")
        self.chord = Track("chord")

    def start(self):
        Metronome().tick_forever()
