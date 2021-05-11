from .metronome import Metronome

import psonic as sp
from math import sin, radians


def kick():
    sp.sample(sp.BD_HAUS, amp=2)
    Metronome().beat_sleep(1)


def snare():
    if Metronome().beat_number % 2 == 0:
        sp.sample(sp.SN_DUB, amp=2)

    Metronome().beat_sleep(wait_len=1)


def perc_setup():
    Metronome().beat_sleep(wait_len=1/2)

def perc():
    sp.sample(sp.DRUM_CYMBAL_CLOSED, rate=2)
    Metronome().beat_sleep(wait_len=1)


def sample():
    sp.sample(sp.VINYL_HISS, rate=7)
    Metronome().beat_sleep(wait_len=2)


def bass():
    min_cutoff = 40
    max_cutoff_diff = 60
    
    cutoff=(min_cutoff + max_cutoff_diff * sin(radians(Metronome().tick_number % 8 * 180 / 8)))
    sp.use_synth(sp.TB303)
    sp.play(sp.E1, release=2, cutoff=cutoff, cutoff_attack=1.5)

    Metronome().beat_sleep(wait_len=4)


def lead():
    pass


def arp():
    play_random_synth_notes = True

    notes = sp.scale(sp.E4 if Metronome().tick_number %
                         8 <= 4 else sp.E5, sp.MINOR_PENTATONIC, num_octaves=2)
    no_of_notes_per_beat = 4
    for i in range(no_of_notes_per_beat):
        sp.use_synth(sp.SINE)
        if play_random_synth_notes:
            note = sp.random.choice(notes)
        else:
            note = notes[i]
        sp.play(note, release=0.1, amp=1.5)

        Metronome().beat_sleep(wait_len=0.25)


def chord():
    pass
