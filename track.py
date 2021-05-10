from .metronome import Metronome
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


class Track:
    TRACK_CLIPS = {
        "kick": kick,
        "snare": snare,
        "perc": perc,
        "sample": sample,
        "bass": bass,
        "lead": lead,
        "arp": arp,
        "chord": chord,
    }

    def __init__(self, id):
        self.enabled = False
        self.clip = Track.TRACK_CLIPS[id]
        self.play_clip()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
    
    @in_thread
    def play_clip(self):
        Metronome().sync()
        while True:
            if self.enabled:
                self.clip()
