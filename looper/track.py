from .metronome import Metronome
from .clips import (
    kick,
    snare,
    perc,
    hiss,
    bass,
    lead,
    arp,
    chord,
)
from threading import Thread


class Track:
    TRACK_CLIPS = {
        "kick": kick,
        "snare": snare,
        "perc": perc,
        "hiss": hiss,
        "bass": bass,
        "lead": lead,
        "arp": arp,
        "chord": chord,
    }

    def __init__(self, id):
        self.enabled = False
        self.clip = Track.TRACK_CLIPS[id]
        self._thread = Thread(target=self.play_clip)

    def enable(self):
        self.enabled = True
        self._thread.start()

    def disable(self):
        self.enabled = False
    
    def play_clip(self):
        Metronome().wait_for_tick()
        while self.enabled:
            self.clip()
