from sequencer.metronome import Metronome

import psonic as sp


def default_chord():
    bar_number = Metronome().bar_number % 4

    chords = [
        sp.chord(sp.C3, sp.MINOR),
        sp.chord(sp.C3, sp.MINOR),
        sp.chord(sp.Ds3, sp.MAJOR),
        sp.chord(sp.As2, sp.MAJOR),
    ]

    sp.use_synth(sp.TB303)
    sp.play(chords[bar_number - 1], amp=1.4, release=1.2)
    Metronome().beat_sleep(wait_len=4)
