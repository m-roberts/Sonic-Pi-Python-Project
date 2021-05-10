import random
from threading import Thread, Event

from .metronome import Metronome
from .tracks import *

# metronome = Metronome(bpm, ticks_per_beat=4)

# kick_track()
# snare_track()
# perc_track()
# sample_track()
# bass_track()
# lead_track()
# arp_track()
# chord_track()

# metronome.tick_forever()


seq = Sequencer()

seq.kick.enable()

seq.snare.enable()
seq.perc.enable()
seq.sample.enable()
seq.bass.enable()
seq.lead.enable()
seq.arp.enable()
seq.chord.enable()

seq.start()
