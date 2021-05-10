from psonic import *
from .clips import (
    kick,
    snare,
    perc,
    sample,
    bass,
    lead,
    arp,
    chord,
)
from .metronome import Metronome

TRACK_CLIPS = {
    Track.KICK: kick,
    Track.SNARE: snare,
    Track.PERC: perc,
    Track.SAMPLE: sample,
    Track.BASS: bass,
    Track.LEAD: lead,
    Track.ARP: arp,
    Track.CHORD: chord,
}

class Track:
    def __init__(self, id):
        self.enabled = False
        self.clip = TRACK_CLIPS[id]

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
    
    @in_thread
    def main_func(self):
        self.metronome.sync()
            while True:
                self.clip()


class Sequencer:
    def __init__(self, metronome=Metronome(bpm, ticks_per_beat=4)):
        self.metronome = metronome

        self.tracks = {
            "kick": Track(Track.KICK, metronome),
            "snare": Track(Track.SNARE, metronome),
            "perc": Track(Track.PERC, metronome),
            "sample": Track(Track.SAMPLE, metronome),
            "bass": Track(Track.BASS, metronome),
            "lead": Track(Track.LEAD, metronome),
            "arp": Track(Track.ARP, metronome),
            "chord": Track(Track.CHORD, metronome),
        }
        self.kick = self.tracks[kick]
        self.snare = self.tracks[snare]
        self.perc = self.tracks[perc]
        self.sample = self.tracks[sample]
        self.bass = self.tracks[bass]
        self.lead = self.tracks[lead]
        self.arp = self.tracks[arp]
        self.chord = self.tracks[chord]

    def start(self):
        self.metronome.tick_forever()
