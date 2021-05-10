from psonic import *
from math import sin, radians
from .clips import *
from .metronome import Metronome


def sync_and_loop(func):
    """Metronome decorator"""

    def wrapper():
        metronome.sync()
        while True:
            func()

    return wrapper

@in_thread
@sync_and_loop
def kick_track():
    kick()

@in_thread
@sync_and_loop
def snare_track():
    snare()
 
@in_thread
@sync_and_loop
def perc_track():
    perc()

@in_thread
@sync_and_loop
def sample_track():
    sample()

@in_thread
@sync_and_loop
def bass_track():
    bass()

@in_thread
@sync_and_loop
def lead_track():
    lead()

@in_thread
@sync_and_loop
def arp_track():
    arp()

@in_thread
@sync_and_loop
def chord_track():
    chord()


class Track:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False


class Sequencer:
    def __init__(self, metronome=Metronome(bpm, ticks_per_beat=4)):
        self.metronome = metronome

        self.tracks = {
            "kick": Track(Track.KICK),
            "snare": Track(Track.SNARE),
            "perc": Track(Track.PERC),
            "sample": Track(Track.SAMPLE),
            "bass": Track(Track.BASS),
            "lead": Track(Track.LEAD),
            "arp": Track(Track.ARP),
            "chord": Track(Track.CHORD),
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
