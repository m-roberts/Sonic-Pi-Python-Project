from sequencer.metronome import Metronome
from .clips import *
from threading import Thread


class Clip:
    def __init__(self, func, beat_offset=0):
        self.func = func
        self.beat_offset = beat_offset


class Track:
    TRACK_CLIPS = {
        "kick": {
            "func": four_to_the_floor,
        },
        "snare": {
            "func": two_beat_snare,
        },
        "perc": {
            "func": one_beat_hi_hat,
            "beat_offset": 1/2,
        },
        "sample": {
            "func": vinyl_hiss,
        },
        "bass": {
            "func": synthwave_offbeat_bass,
        },
        "lead": {
            "func": whimsical_melody_lead,
        },
        "arp": {
            "func": three_quarter_notes_descending_arp,
        },
        "chord": {
            "func": simple_four_chords,
        },
    }

    def __init__(self, id):
        self.id = id
        self.enabled = False

        current_clip = Track.TRACK_CLIPS.get(id, dict())
        self.clip = Clip(current_clip.get("func", None), current_clip.get("beat_offset", 0))

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
        Metronome().beat_sleep(self.clip.beat_offset)

        if self.id == "perform":
            while True:
                while not callable(self.clip.func):
                    Metronome().wait_for_tick()

                self.clip.func()
                self.clip.func = None
        else:
            while self.enabled:
                if callable(self.clip.func):
                    self.clip.func()
