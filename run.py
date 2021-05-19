from sequencer import *
from psonic import *

seq = Sequencer(bpm=108)


def intro():
    seq.enable_tracks([seq.kick, seq.sample, seq.bass])
    seq.kick.clip = Clip(quiet_kick)

def start_snare():
    seq.enable_tracks(seq.snare)
    seq.perform.clip = Clip(open_cymbal)

def start_perc():
    seq.enable_tracks(seq.perc)

def stop_perc():
    seq.disable_tracks(seq.perc)

def first_chorus():
    seq.enable_tracks(seq.all_tracks)
    seq.disable_tracks(seq.sample)

    seq.perform.clip = Clip(open_cymbal)
    seq.kick.clip = Clip(four_to_the_floor)
    seq.perc.clip = Clip(quarter_note_closed_cymbals)

def breakdown():
    seq.enable_tracks([seq.bass, seq.perc, seq.arp, seq.chord], exclusive=True)

def outro():
    seq.enable_tracks(seq.all_tracks)

    def outro_kick():
        for i in [1, 1, 0.5, 0.5, 1]:
            sp.sample(sp.BD_HAUS, amp=1.5)
            Metronome().beat_sleep(i)

    seq.kick.clip = Clip(outro_kick)
    seq.perform.clip = Clip(open_cymbal)
    seq.perc.clip = Clip(one_beat_hi_hat, offset=1/2)

seq.register_event(intro,        bar=1)
seq.register_event(start_snare,  bar=4, beat=4)
seq.register_event(start_perc,   bar=9)
seq.register_event(first_chorus, bar=17)
seq.register_event(breakdown,    bar=25)
seq.register_event(stop_perc,    bar=31)
seq.register_event(outro,        bar=33)
seq.set_length(40)
seq.start()
