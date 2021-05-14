from sequencer.metronome import Metronome

import psonic as sp


def open_cymbal():
    sp.sample(sp.DRUM_CYMBAL_OPEN)
