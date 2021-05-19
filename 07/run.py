from track import LoopingTrack

from psonic import *


# Basic drum loop
while True:
    sample(BD_HAUS)
    sleep(0.5)
    sample(BD_HAUS)
    sample(SN_DUB)
    sleep(0.5)



# Separate into functions - doesn't yet work!
def kick_loop():
    sample(BD_HAUS)
    sleep(0.5)

def snare_loop():
    sample(SN_DUB)
    sleep(1)


while True:
    kick()
    snare()

# We need to define some new behaviour.
# We want these functions to be called over and over...

# Switch to track.py to implement the looping logic that we want...

kick_track = LoopingTrack(kick_loop)
snare_track = LoopingTrack(snare_loop)

button.wait_for_press()

# We have 2 tracks! But they aren't synchronised... we need a conductor!

# Now add metronome (metronome.py)...
# Now update LoopingTrack to use metronome...
# Now add a third track

def perc_loop():
    sample(DRUM_CYMBAL_CLOSED)
    sleep(0.25)

perc_track = LoopingTrack(perc_loop)

# Let's make it a bit more interesting...
