from sequencer.metronome import Metronome

import psonic as sp


def default_bass():
    bar_number = Metronome().bar_number % 4
    notes = [sp.C1, sp.C1, sp.Ds1, sp.As0]

    Metronome().beat_sleep(wait_len=1/4)
    for _ in range(3):
        sp.use_synth(sp.TB303)
        octave_notes = [notes[bar_number - 1], notes[bar_number - 1]+ 12]
        sp.play(
            octave_notes,
            sustain=0.1,
            release=0.1,
            amp=0.9,
            cutoff=110
        )
        Metronome().beat_sleep(wait_len=1/4)
