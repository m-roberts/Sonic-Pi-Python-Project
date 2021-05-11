from looper.sequencer import Sequencer
from psonic import *

seq = Sequencer(bpm=108)

# Enable tracks
seq.kick.enable()
seq.snare.enable()
seq.perc.enable()
# seq.sample.enable()
seq.bass.enable()
seq.lead.enable()
seq.arp.enable()
seq.chord.enable()

# Override default perc behaviour
def perc_setup():
    seq.metronome.beat_sleep(wait_len=1/2)

def perc():
    sample(DRUM_CYMBAL_CLOSED, amp=2.5)
    seq.metronome.beat_sleep(wait_len=1)

seq.perc.setup = perc_setup
seq.perc.clip = perc

try:
    seq.start()
except Exception:
    seq.stop()
