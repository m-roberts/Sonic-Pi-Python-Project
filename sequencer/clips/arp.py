from sequencer.metronome import Metronome

import psonic as sp


def default_arp():
    notes = sp.scale(
        root_note=sp.C5,
        scale_mode=sp.MINOR_PENTATONIC,
        num_octaves=1
    )
    for i in range(3):
        sp.use_synth(sp.SINE)
        sp.play(notes[-(i+1)], release=0.1, amp=0.5)

        Metronome().beat_sleep(wait_len=0.25)
