from pitop import Button
from psonic import play, scale, C4, MAJOR

btn = Button("D0")


# Use a button to trigger a note
while True:
    if btn.is_pressed:
        play(60)
    sleep(0.5)

# Use a button to start a loop
btn.wait_for_press()
while True:
    play(60)
    sleep(0.5)


# Use a button to start playing the notes in a scale

while True:
    btn.wait_for_press()

    for note in scale(C4, MAJOR):
      play(note)
      sleep(0.5)

# Change root note; change scale
root_note = C4
scale = MAJOR

while True:
    btn.wait_for_press()

    for note in scale(root_note, scale):
      play(note)
      sleep(0.5)

    root_note = root_note + 1
    if scale == MAJOR:
        scale = MINOR
    else:
        scale = MAJOR
