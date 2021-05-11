from sequencer.metronome import Metronome

import psonic as sp


def default_lead_setup():
    Metronome().beat_sleep(wait_len=1)

def default_lead():
    notes = [
        # bar 1
        (sp.Ds4, 1),
        (sp.C4, 1),
        (sp.As4, 1/4),
        (sp.C4, 3/4),
        # bar 2
        (sp.C4, 1),
        (sp.Ds4, 1),
        (sp.C4, 1),
        (None, 2),
        # bar 3
        (sp.Ds4, 1),
        (sp.C4, 1),
        (sp.As4, 1/4),
        (sp.C4, 3/4),
        # bar 4
        (sp.C4, 1),
        (sp.Ds4, 1),
        (sp.C4, 1),
        (sp.As4, 2),
    ]
    
    for note in notes:
        sp.use_synth(sp.PLUCK)
        sp.play(note[0], amp=2)
        Metronome().beat_sleep(note[1])
