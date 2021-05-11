from .metronome import Metronome
from .track import Track
from psonic import in_thread


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

        self.tracks = [
            self.kick,
            self.snare,
            self.perc,
            self.sample,
            self.bass,
            self.lead,
            self.arp,
            self.chord
        ]

    def start(self):
        self.metronome.tick_forever()

    def stop(self):
        self.disable_all()

    def enable_all(self):
        for track in self.tracks:
            track.enable()
                
    def disable_all(self):
        for track in self.tracks:
            track.disable()
