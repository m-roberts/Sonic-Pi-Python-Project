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
    seq.kick.clip = Clip(quiet_kick)

    seq.sample.enable()
    seq.bass.enable()

def start_snare():
    seq.snare.enable()

    seq.perform.clip = Clip(open_cymbal)

def start_perc():
    seq.perc.enable()

def stop_perc():
    seq.perc.disable()

def first_chorus():
    seq.enable_all()

    seq.perform.clip = Clip(open_cymbal)

    seq.kick.clip = Clip(four_to_the_floor)

    seq.perc.clip = Clip(quarter_note_closed_cymbals)

    seq.sample.disable()

def breakdown():
    seq.disable_all()

    seq.bass.enable()
    seq.perc.enable()
    seq.arp.enable()
    seq.chord.enable()

def outro_kick():
    for i in [1, 1, 0.5, 0.5, 1]:
      sp.sample(sp.BD_HAUS, amp=1.5)
      Metronome().beat_sleep(i)

def outro():
    seq.enable_all()
    seq.kick.clip = Clip(outro_kick)
    seq.perform.clip = Clip(open_cymbal)
    seq.perc.clip = Clip(one_beat_hi_hat, 1/2)

sections = {
    (1,  1, 1): intro,
    (4,  4, 1): start_snare,
    (9,  1, 1): start_perc,
    (17, 1, 1): first_chorus,
    (25, 1, 1): breakdown,
    (31, 1, 1): stop_perc,
    (33, 1, 1): outro,
    (41, 1, 1): exit,
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
