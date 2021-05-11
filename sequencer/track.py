from sequencer.metronome import Metronome
from .clips import *
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
            "setup": default_perc_setup,
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
        "perform": {
            "clip": None,
            "setup": None,
        },
    }

    def __init__(self, id):
        self.id = id
        self.enabled = False
        self.setup = Track.TRACK_CLIPS[id]["setup"]
        self.clip = Track.TRACK_CLIPS[id]["clip"]
        self._thread = None

    def start_thread(self):
        self.stop_thread()
        self._thread = Thread(target=self.play_clip)
        self._thread.start()

    def stop_thread(self, timeout=0):
        if isinstance(self._thread, Thread) and self._thread.is_alive():
            self._thread.join(timeout)

    def enable(self):
        if not self.enabled:
            self.enabled = True
            self.start_thread()

    def disable(self):
        self.enabled = False
        self.stop_thread()

    def play_clip(self):
        Metronome().wait_for_tick()
        if callable(self.setup):
            self.setup()

        if self.id == "perform":
            while True:
                while not callable(self.clip):
                    Metronome().wait_for_tick()

                self.clip()
                self.clip = None
        else:
            while self.enabled:
                if callable(self.clip):
                    self.clip()
