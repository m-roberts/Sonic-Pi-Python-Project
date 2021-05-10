from .metronome import Metronome
from .track import Track


class Sequencer:
    TRACKS = {
        "kick": Track(Track.KICK, metronome),
        "snare": Track(Track.SNARE, metronome),
        "perc": Track(Track.PERC, metronome),
        "sample": Track(Track.SAMPLE, metronome),
        "bass": Track(Track.BASS, metronome),
        "lead": Track(Track.LEAD, metronome),
        "arp": Track(Track.ARP, metronome),
        "chord": Track(Track.CHORD, metronome),
    }

    def __init__(self, bpm=120, ticks_per_beat=4):
        Metronome().bpm = bpm
        Metronome().ticks_per_beat = ticks_per_beat
        self.kick = Sequencer.TRACKS[kick]
        self.snare = Sequencer.TRACKS[snare]
        self.perc = Sequencer.TRACKS[perc]
        self.sample = Sequencer.TRACKS[sample]
        self.bass = Sequencer.TRACKS[bass]
        self.lead = Sequencer.TRACKS[lead]
        self.arp = Sequencer.TRACKS[arp]
        self.chord = Sequencer.TRACKS[chord]

    def start(self):
        Metronome().tick_forever()
