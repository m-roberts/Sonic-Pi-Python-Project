from sequencer.metronome import Metronome

import psonic as sp


def vinyl_hiss():
    sp.sample(sp.VINYL_HISS, rate=7, amp=3)
    Metronome().beat_sleep(wait_len=2)
