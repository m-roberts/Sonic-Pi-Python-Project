from looper.sequencer import Sequencer
from psonic import *

seq = Sequencer(bpm=108)

seq.kick.enable()
seq.snare.enable()
seq.perc.enable()
# seq.sample.enable()
seq.bass.enable()
seq.lead.enable()
seq.arp.enable()
seq.chord.enable()

try:
    seq.start()
except Exception:
    seq.stop()
