from track import LoopingTrack
from metronome import Metronome

from psonic import *


# We want to be able to change the speed.
# We could go in and change every "sleep()" function...
# OR we can create some code that handles BPM!

# go to metronome.py, update to include support for BPM

metronome = Metronome(bpm=108)

def kick_loop():
    sample(BD_HAUS)
    sleep(0.5)


def snare_loop():
    sample(SN_DUB)
    sleep(1)


def perc_loop():
    sample(DRUM_CYMBAL_CLOSED)
    sleep(0.25)


kick_track = LoopingTrack(kick_loop)
snare_track = LoopingTrack(snare_loop)
perc_track = LoopingTrack(perc_loop)

button.wait_for_press()


# Let's change the BPM with a potentiometer...
# TODO


# Now let's add some chords!

# And a bass!

# ALL THE THINGS!
