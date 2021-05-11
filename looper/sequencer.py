from .metronome import Metronome
from .track import Track


class Sequencer:
    def __init__(self, bpm=120, ticks_per_beat=4):
        self.metronome = Metronome(bpm, ticks_per_beat)

        self.kick = Track("kick")
        self.snare = Track("snare")
        self.perc = Track("perc")
        self.sample = Track("sample")
        self.bass = Track("bass")
        self.lead = Track("lead")
        self.arp = Track("arp")
        self.chord = Track("chord")

    def start(self):
        self.metronome.tick_forever()

    def stop(self):
        self.kick.disable()
        self.snare.disable()
        self.perc.disable()
        self.sample.disable()
        self.bass.disable()
        self.lead.disable()
        self.arp.disable()
        self.chord.disable()
