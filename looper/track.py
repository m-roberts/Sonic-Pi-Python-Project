from .metronome import Metronome
from .clips import (
    default_kick,
    default_snare,
    default_perc,
    default_sample,
    default_bass,
    default_lead,
    default_lead_setup,
    default_arp,
    default_chord,
)
from threading import Thread


class Track:
    TRACK_CLIPS = {
        "kick": {
            "clip": default_kick,
            "setup": None,
        },
        "snare": {
            "clip": default_snare,
            "setup": None,
        },
        "perc": {
            "clip": default_perc,
            "setup": None,
        },
        "sample": {
            "clip": default_sample,
            "setup": None,
        },
        "bass": {
            "clip": default_bass,
            "setup": None,
        },
        "lead": {
            "clip": default_lead,
            "setup": default_lead_setup,
        },
        "arp": {
            "clip": default_arp,
            "setup": None,
        },
        "chord": {
            "clip": default_chord,
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
