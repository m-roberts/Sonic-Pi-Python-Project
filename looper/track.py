from .metronome import Metronome
from .clips import (
    kick,
    snare,
    perc,
    perc_setup,
    sample,
    bass,
    lead,
    lead_setup,
    arp,
    chord,
)
from threading import Thread


class Track:
    TRACK_CLIPS = {
        "kick": {
            "clip": kick,
            "setup": None,
        },
        "snare": {
            "clip": snare,
            "setup": None,
        },
        "perc": {
            "clip": perc,
            "setup": perc_setup,
        },
        "sample": {
            "clip": sample,
            "setup": None,
        },
        "bass": {
            "clip": bass,
            "setup": None,
        },
        "lead": {
            "clip": lead,
            "setup": lead_setup,
        },
        "arp": {
            "clip": arp,
            "setup": None,
        },
        "chord": {
            "clip": chord,
            "setup": None,
        },
    }

    def __init__(self, id):
        self.enabled = False
        self.setup = Track.TRACK_CLIPS[id]["setup"]
        self.clip = Track.TRACK_CLIPS[id]["clip"]
        self._thread = Thread(target=self.play_clip)

    def enable(self):
        self.enabled = True
        self._thread.start()

    def disable(self):
        self.enabled = False
    
    def play_clip(self):
        Metronome().wait_for_tick()
        if callable(self.setup):
            self.setup()

        while self.enabled:
            self.clip()
