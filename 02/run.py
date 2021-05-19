from pitop import Button
from psonic import play

# BEEP: Play a sound
play(70)


# Change the number - change the note
play(75)

play(65)


# lower numbers make lower pitched beeps and higher numbers make higher pitched beeps


# CHORDS: Play multiple sounds at once
play(72)
play(75)
play(79)

# which numbers sound good together? which don't?


# MELODY: separating notes in time by sleeping
# (notes on what an arpeggio is)
play(72)
sleep(1)
play(75)
sleep(1)
play(79)


# Change the sleep time - change the speed
play(72)
sleep(0.5)
play(75)
sleep(0.5)
play(79)


# Play around with in-between notes
play(52.3)


# NOTATION: Using traditional note names
play(:C)
sleep(0.5)
play(:D)
sleep(0.5)
play(:E)

# Define octave:
play(:C3)
sleep(0.5)
play(:D3)
sleep(0.5)
play(:E3)

# Change the octave, change the pitch:
play(:C2)
sleep(0.5)
play(:D3)
sleep(0.5)
play(:E4)

# 'Sharp'/'flat' notes (black keys on a piano) can be played too:
play(:Fs3)
play(:Eb3)


# USING TRADITIONAL NOTATION FOR CHORDS
chord(:E3, :minor)



# Twinkle twinkle - (using note syntax!)

while True:
    play(C3)
    sleep(0.5)
    play(C3)
    sleep(0.5)
    play(G3)
    sleep(0.5)
    play(G3)
    sleep(0.5)
    play(A3)
    sleep(0.5)
    play(A3)
    sleep(0.5)
    play(G3)
    sleep(1.0)

    play(F3)
    sleep(0.5)
    play(F3)
    sleep(0.5)
    play(E3)
    sleep(0.5)
    play(E3)
    sleep(0.5)
    play(D3)
    sleep(0.5)
    play(D3)
    sleep(0.5)
    play(C3)
    sleep(1.0)
