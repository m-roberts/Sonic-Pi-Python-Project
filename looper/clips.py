from .metronome import Metronome

from psonic import *
from math import sin, radians


def kick():
    sample(BD_HAUS, amp=2)
    Metronome().beat_sleep(1)


def snare():
    if Metronome().tick_number % 2 == 0:
        sample(SN_DUB, amp=2)

    Metronome().beat_sleep(wait_len=1)


def perc():
    if Metronome().tick_number % 4 == 2:
        sample(DRUM_CYMBAL_CLOSED, rate=2)
    if Metronome().tick_number % 4 == 4:
        sample(DRUM_SPLASH_SOFT, rate=2)

    Metronome().beat_sleep(wait_len=1/2)


def hiss():
    sample(VINYL_HISS, amp=5, rate=7)
    Metronome().beat_sleep(wait_len=2)


def bass():
    min_cutoff = 40
    max_cutoff_diff = 60
    
    cutoff=(min_cutoff + max_cutoff_diff * sin(radians(Metronome().tick_number % 8 * 180 / 8)))
    use_synth(TB303)
    play(E1, release=2, cutoff=cutoff, cutoff_attack=1.5)

    Metronome().beat_sleep(wait_len=4)


def lead():
    pass


def arp():
    play_random_synth_notes = True

    notes = scale(E4 if Metronome().tick_number % 8 <= 4 else E5, MINOR_PENTATONIC, num_octaves=2)
    no_of_notes_per_beat = 4
    for i in range(no_of_notes_per_beat):
        use_synth(SINE)
        if play_random_synth_notes:
            note = random.choice(notes)
        else:
            note = notes[i]
        play(note, release=0.1, amp=1.5)

        Metronome().beat_sleep(wait_len=0.25)


def chord():
    pass
