from sequencer import *
from psonic import *
from sys import exit

seq = Sequencer(bpm=108)

# Run loops forever...
# seq.enable_all()
# seq.start()

# Or handle sections manually...
def intro():
    seq.kick.enable()
    seq.kick.clip = quiet_kick

    seq.sample.enable()
    seq.bass.enable()

def start_snare():
    seq.snare.enable()

    seq.perform.clip = open_cymbal

def start_perc():
    seq.perc.enable()

def stop_perc():
    seq.perc.disable()

def first_chorus():
    seq.enable_all()

    seq.perform.clip = open_cymbal

    seq.kick.clip = default_kick

    seq.perc.clip = quarter_note_closed_cymbals
    seq.perc.setup = None

    seq.sample.disable()

def breakdown():
    seq.disable_all()

    seq.bass.enable()
    seq.perc.enable()
    seq.arp.enable()
    seq.chord.enable()

def outro():
    seq.enable_all()
    seq.perform.clip = open_cymbal
    seq.perc.clip = default_perc
    seq.perc.setup = default_perc_setup

sections = {
    (1,  1, 1): intro,
    (4,  4, 1): start_snare,
    (9,  1, 1): start_perc,
    (17, 1, 1): first_chorus,
    (25, 1, 1): breakdown,
    (31, 1, 1): stop_perc,
    (33, 1, 1): outro,
    (41, 1, 1): lambda: exit(),
}
metronome = seq.metronome

while True:
    metronome.tick()

    print(metronome.tick_tuple)
    if metronome.tick_tuple in sections:
        func = sections[metronome.tick_tuple]
        if callable(func):
            func()

    metronome.cue()
    metronome.tick_sleep()
