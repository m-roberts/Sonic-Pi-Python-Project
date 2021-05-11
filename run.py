from looper.sequencer import Sequencer
from signal import pause
from psonic import *

seq = Sequencer(bpm=108)
metronome = seq.metronome

# Override default perc behaviour
def perc_setup():
    metronome.beat_sleep(wait_len=1/2)

def perc():
    sample(DRUM_CYMBAL_CLOSED, amp=2.5)
    metronome.beat_sleep(wait_len=1)

seq.perc.setup = perc_setup
seq.perc.clip = perc

# Run loops forever...
# seq.enable_all()
# seq.start()

# Or handle sections manually...
while True:
    metronome.tick()
    if metronome.is_new_bar:

        if metronome.bar_number == 1:
            seq.kick.enable()
            seq.sample.enable()
            seq.bass.enable()

        elif metronome.bar_number == 9:
            seq.snare.enable()

        elif metronome.bar_number == 13:
            seq.perc.enable()

        elif metronome.bar_number == 17:
            seq.enable_all()
            seq.sample.disable()

        elif metronome.bar_number == 25:
            seq.disable_all()

            seq.bass.enable()
            seq.perc.enable()
            seq.arp.enable()
            seq.chord.enable()
        elif metronome.bar_number == 31:
            seq.perc.disable()

        elif metronome.bar_number == 33:
            seq.enable_all()

        elif metronome.bar_number == 41:
            seq.disable_all()

    metronome.cue()
    metronome.tick_sleep()
