from sequencer import *
from psonic import *
from pitop import Button, Potentiometer

seq = Sequencer(bpm=108)

btn = Button("D0")
pot = Potentiometer("A0")

kick_mute = False


def toggle_mute():
    global kick_mute
    kick_mute = not kick_mute

btn.when_activated = toggle_mute


def my_mutable_four_to_the_floor():
    if not kick_mute:
        sp.sample(sp.BD_HAUS, amp=2.5)
    Metronome().beat_sleep(1)


def three_quarter_notes_descending_arp_with_release_control():
    notes = sp.scale(
        root_note=sp.C5,
        scale_mode=sp.MINOR_PENTATONIC,
        num_octaves=1
    )
    for i in range(3):
        sp.use_synth(sp.SINE)
        sp.play(notes[-(i+1)], release=pot.position/1000.0*0.8, amp=0.5)

        Metronome().beat_sleep(wait_len=0.25)


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
    seq.kick.clip = Clip(my_mutable_four_to_the_floor)
    seq.perc.clip = Clip(quarter_note_closed_cymbals)

def breakdown():
    seq.arp.clip = Clip(three_quarter_notes_descending_arp_with_release_control)
    seq.enable_tracks([seq.bass, seq.perc, seq.arp, seq.chord], exclusive=True)

def outro():
    seq.enable_tracks(seq.all_tracks)

    def outro_kick():
        for i in [1, 1, 0.5, 0.5, 1]:
            sp.sample(sp.BD_HAUS, amp=1.5)
            Metronome().beat_sleep(i)

    seq.kick.clip = Clip(outro_kick)
    seq.perform.clip = Clip(open_cymbal)
    seq.perc.clip = Clip(one_beat_hi_hat, 1/2)

seq.register_event(first_chorus, bar=1)
seq.start()
