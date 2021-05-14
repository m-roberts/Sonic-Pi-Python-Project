from sequencer.metronome import Metronome

import psonic as sp


def quiet_kick():
    sp.sample(sp.BD_HAUS, amp=1.5)
    Metronome().beat_sleep(1)


def four_to_the_floor():
    sp.sample(sp.BD_HAUS, amp=2.5)
    Metronome().beat_sleep(1)
