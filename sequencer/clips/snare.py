from sequencer.metronome import Metronome

import psonic as sp
from time import sleep


def two_beat_snare():
    if Metronome().beat_number % 2 == 0:
        sleep(0.005)
        sp.sample(sp.SN_DUB, amp=2)

    Metronome().beat_sleep(wait_len=1)
