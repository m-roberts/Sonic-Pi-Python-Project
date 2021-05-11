from .metronome import Metronome

import psonic as sp
from math import sin, radians
from time import sleep


def default_kick():
    sp.sample(sp.BD_HAUS, amp=2.5)
    Metronome().beat_sleep(1)


def default_snare():
    if Metronome().beat_number % 2 == 0:
        sleep(0.005)
        sp.sample(sp.SN_DUB, amp=2)

    Metronome().beat_sleep(wait_len=1)


def default_perc():
    sp.sample(sp.DRUM_CYMBAL_CLOSED, amp=2.5)
    Metronome().beat_sleep(wait_len=1/4)


def default_sample():
    sp.sample(sp.VINYL_HISS, rate=7, amp=7)
    Metronome().beat_sleep(wait_len=2)


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
