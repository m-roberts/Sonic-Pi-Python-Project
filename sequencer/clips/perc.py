from sequencer.metronome import Metronome

import psonic as sp


def one_beat_hi_hat():
    sp.sample(sp.DRUM_CYMBAL_CLOSED, amp=2.5)
    Metronome().beat_sleep(wait_len=1)


def quarter_note_closed_cymbals():
    sp.sample(sp.DRUM_CYMBAL_CLOSED, amp=2.5)
    Metronome().beat_sleep(wait_len=1/4)
