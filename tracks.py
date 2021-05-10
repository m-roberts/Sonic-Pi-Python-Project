from psonic import *
from math import sin, radians
from .clips import *

def init_sync(func):
    """Metronome decorator"""

    def wrapper():
        metronome.sync()
        func()

    return wrapper

@in_thread
@init_sync
def kick_drum_track():
    while True:
        kick_drum()

@in_thread
@init_sync
def hi_hat_track():
    hh_beat_no = 0
    while True:
        hh_beat_no = 1 if hh_beat_no == 4 else hh_beat_no + 1
        if hh_beat_no == 2:
            sample(DRUM_CYMBAL_CLOSED, rate=2)
        if hh_beat_no == 4:
            sample(DRUM_SPLASH_SOFT, rate=2)
        beat_sleep(wait_len=1/2)

@in_thread
@init_sync
def snare_track():
    snare_beat_no = 0
    while True:
        snare_beat_no = 1 if snare_beat_no == 4 else snare_beat_no + 1
        if snare_beat_no % 2 == 0:
            sample(SN_DUB, amp=2)
        beat_sleep(wait_len=1)

@in_thread
@init_sync
def vinyl_hiss_track():
    while True:
        sample(VINYL_HISS, amp=5, rate=7)
        beat_sleep(wait_len=2)

@in_thread
@init_sync
def synth_wub_track():
    sin_step = 0
    total_steps = 8
    min_cutoff = 40
    max_cutoff_diff = 60
    while True:
        sin_step = sin_step + 1
        cutoff=(min_cutoff + max_cutoff_diff * sin(radians(sin_step * 180 / total_steps)))
        use_synth(TB303)
        play(E1, release=2, cutoff=cutoff, cutoff_attack=1.5)
        beat_sleep(wait_len=4)

@in_thread
@init_sync
def synth_plucks_track():
    loop_no = 0
    play_random_synth_notes = False

    while True:
        loop_no = 0 if loop_no == 8 else loop_no + 1
        notes = scale(E4 if loop_no <= 4 else E5, MINOR_PENTATONIC, num_octaves=2)
        no_of_notes_per_beat = 4
        for i in range(no_of_notes_per_beat):
            use_synth(SINE)
            if play_random_synth_notes:
                note = random.choice(notes)
            else:
                note = notes[i]
            play(note, release=0.1, amp=1.5)
            beat_sleep(wait_len=0.25)
