import random
from threading import Thread, Event

from .metronome import Metronome
from .tracks import *

metronome = Metronome(bpm, ticks_per_beat=4)

############
# Let's go #
############
kick_drum_track()
hi_hat_track()
snare_track()
vinyl_hiss_track()
synth_wub_track()
synth_plucks_track()

metronome.tick_forever()
