from sequencer.metronome import Metronome

import psonic as sp


def default_sample():
    sp.sample(sp.VINYL_HISS, rate=7, amp=7)
    Metronome().beat_sleep(wait_len=2)
