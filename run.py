from sequencer import Sequencer
from track import Clip
from metronome import Metronome

from pitop import Potentiometer
from psonic import *


metronome = Metronome(bpm=108)
seq = Sequencer(metronome)

###########################
# DEFINE GLOBAL VARIABLES #
###########################
kick_amp = 2.5
pot = Potentiometer("A0")

################
# DEFINE LOOPS #
################

# Kick
def four_to_the_floor():
    sample(BD_HAUS, amp=kick_amp)
    metronome.beat_sleep(1)

def outro_kick():
    for i in [1, 1, 0.5, 0.5, 1]:
        sp.sample(sp.BD_HAUS, amp=kick_amp)
        metronome.beat_sleep(i)

# Snare
def offbeat_snare():
    if metronome.beat_number % 2 == 0:
        sleep(0.005)
        sample(SN_DUB, amp=2)

    metronome.beat_sleep(1)

# Perc
def one_beat_hi_hat():
    sample(DRUM_CYMBAL_CLOSED, amp=2.5)
    metronome.beat_sleep(1)

def quarter_note_closed_cymbals():
    sample(DRUM_CYMBAL_CLOSED, amp=2.5)
    metronome.beat_sleep(1/4)

# Sample
def vinyl_hiss():
    sample(VINYL_HISS, rate=7, amp=3)
    metronome.beat_sleep(2)

# Bass
def synthwave_offbeat_bass():
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
def whimsical_melody_lead():
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
def three_quarter_notes_descending_arp():
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
def simple_four_chords():
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

# Define initial clips
seq.kick.clip = Clip(four_to_the_floor)
seq.snare.clip = Clip(offbeat_snare)
seq.perc.clip = Clip(one_beat_hi_hat, beat_offset=1/2)
seq.sample.clip = Clip(vinyl_hiss)
seq.bass.clip = Clip(synthwave_offbeat_bass)
seq.lead.clip = Clip(whimsical_melody_lead)
seq.arp.clip = Clip(three_quarter_notes_descending_arp)
seq.chord.clip = Clip(simple_four_chords)

############
# SECTIONS #
############
def intro():
    seq.enable_tracks([seq.kick, seq.sample, seq.bass])
    kick_amp = 1.5

def start_snare():
    seq.enable_tracks(seq.snare)

    # Perform one-shot cymbal hit
    seq.perform.clip = Clip(open_cymbal)

def start_perc():
    seq.enable_tracks(seq.perc)

def stop_perc():
    seq.disable_tracks(seq.perc)

def first_chorus():
    global kick_amp

    # Enable all tracks except for sample
    seq.enable_tracks(seq.all_tracks)
    seq.disable_tracks(seq.sample)

    # Perform one-shot cymbal hit
    seq.perform.clip = Clip(open_cymbal)
    seq.kick.clip = Clip(four_to_the_floor)
    kick_amp = 2.5

    seq.perc.clip = Clip(quarter_note_closed_cymbals)

def breakdown():
    # Only play these specific tracks
    seq.enable_tracks([seq.bass, seq.perc, seq.arp, seq.chord], exclusive=True)

def outro():
    seq.enable_tracks(seq.all_tracks)

    seq.kick.clip = Clip(outro_kick)
    seq.perform.clip = Clip(open_cymbal)
    seq.perc.clip = Clip(one_beat_hi_hat, 1/2)

# Register track change events
seq.register_event(intro,        bar=1)
seq.register_event(start_snare,  bar=4, beat=4)
seq.register_event(start_perc,   bar=9)
seq.register_event(first_chorus, bar=9)
seq.register_event(breakdown,    bar=25)
seq.register_event(stop_perc,    bar=31)
seq.register_event(outro,        bar=33)
seq.set_length(40)
seq.start()
