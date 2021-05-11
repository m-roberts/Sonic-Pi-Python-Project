from sequencer.metronome import Metronome

import psonic as sp


def quiet_kick():
    sp.sample(sp.BD_HAUS, amp=1.5)
    Metronome().beat_sleep(1)


def default_kick():
    sp.sample(sp.BD_HAUS, amp=2.5)
    Metronome().beat_sleep(1)
