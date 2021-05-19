from track import Clip, Track
from metronome import Metronome

from pitop import Potentiometer
from psonic import *


metronome = Metronome(bpm=108)

###########################
# DEFINE GLOBAL VARIABLES #
###########################
kick_amp = 2.5
pot = Potentiometer("A0")

################
# DEFINE LOOPS #
################

# Kick
def four_to_the_floor(metronome):
    sample(BD_HAUS, amp=kick_amp)
    metronome.beat_sleep(1)

def outro_kick(metronome):
    for i in [1, 1, 0.5, 0.5, 1]:
        sp.sample(sp.BD_HAUS, amp=kick_amp)
        metronome.beat_sleep(i)

# Snare
def offbeat_snare(metronome):
    if metronome.beat_number % 2 == 0:
        sleep(0.005)
        sample(SN_DUB, amp=2)

    metronome.beat_sleep(1)

# Perc
def one_beat_hi_hat(metronome):
    sample(DRUM_CYMBAL_CLOSED, amp=2.5)
    metronome.beat_sleep(1)

def quarter_note_closed_cymbals(metronome):
    sample(DRUM_CYMBAL_CLOSED, amp=2.5)
    metronome.beat_sleep(1/4)

# Sample
def vinyl_hiss(metronome):
    sample(VINYL_HISS, rate=7, amp=3)
    metronome.beat_sleep(2)

# Bass
def synthwave_offbeat_bass(metronome):
    bar_number = metronome.bar_number % 4
    notes = [C1, C1, Ds1, As0]

    metronome.beat_sleep(1/4)
    for _ in range(3):
        use_synth(TB303)
        octave_notes = [notes[bar_number - 1], notes[bar_number - 1]+ 12]
        play(
            octave_notes,
            sustain=0.1,
            release=0.1,
            amp=0.9,
            cutoff=110
        )
        metronome.beat_sleep(1/4)

# Lead
def whimsical_melody_lead(metronome):
    notes = [
        # bar 1
        (None, 1),
        (Ds4, 1),
        (C4, 1),
        (As4, 1/4),
        (C4, 3/4),
        # bar 2
        (C4, 1),
        (Ds4, 1),
        (C4, 1),
        (None, 1),
        # bar 3
        (None, 1),
        (Ds4, 1),
        (C4, 1),
        (As4, 1/4),
        (C4, 3/4),
        # bar 4
        (C4, 1),
        (Ds4, 1),
        (C4, 1),
        (As4, 1),
    ]
    
    for note in notes:
        use_synth(PLUCK)
        play(note[0], amp=2)
        metronome.beat_sleep(note[1])

# Arp
def three_quarter_notes_descending_arp(metronome):
    notes = scale(
        root_note=C5,
        scale_mode=MINOR_PENTATONIC,
        num_octaves=1
    )
    for i in range(3):
        use_synth(SINE)
        play(notes[-(i+1)], release=0.7 * pot.position / 1000, amp=0.5)

        metronome.beat_sleep(0.25)

# Chord
def simple_four_chords(metronome):
    bar_number = metronome.bar_number % 4

    chords = [
        chord(C3, MINOR),
        chord(C3, MINOR),
        chord(Ds3, MAJOR),
        chord(As2, MAJOR),
    ]

    use_synth(TB303)
    play(chords[bar_number - 1], amp=1.4, release=1.2)
    metronome.bar_sleep(1)

# Create tracks
kick_track   = Track(four_to_the_floor,                  metronome)
snare_track  = Track(offbeat_snare,                      metronome)
perc_track   = Track(one_beat_hi_hat,                    metronome, beat_offset=1/2)
sample_track = Track(vinyl_hiss,                         metronome)
bass_track   = Track(synthwave_offbeat_bass,             metronome)
lead_track   = Track(whimsical_melody_lead,              metronome)
arp_track    = Track(three_quarter_notes_descending_arp, metronome)
chord_track  = Track(simple_four_chords,                 metronome)


while True:
    metronome.tick()
    metronome.cue()
    metronome.tick_sleep()
