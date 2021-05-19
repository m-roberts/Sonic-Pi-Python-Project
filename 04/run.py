from pitop import Button, UltrasonicSensor
from psonic import play, scale, C4, MAJOR

import random

btn = Button("D0")
sensor = UltrasonicSensor("D0")

# Use a button to start a synth loop with volume controlled by Ultrasonic sensor
while True:
    btn.wait_for_press()

    for note in scale(C4, MAJOR):
      play(note, amp=sensor.value * 2)
      sleep(0.5)


# Random panning 0 to 1 (center to right)
while True:
    btn.wait_for_press()

    for note in scale(C4, MAJOR):
      play(note, amp=sensor.value * 2, pan=random.random())
      sleep(0.5)


# Correcting for -1 to 1 (left to right)
while True:
    btn.wait_for_press()

    for note in scale(C4, MAJOR):
      play(note, amp=sensor.value * 2, pan=(random.random() * 2 - 1))
      sleep(0.5)


# Applying randomness to cutoff of twinkle twinkle
while True:
    play(C3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(C3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(G3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(G3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(A3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(A3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(G3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(1.0)

    play(F3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(F3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(E3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(E3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(D3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(D3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(0.5)
    play(C3, amp=sensor.value * 2, cutoff=random.rrand(70, 130))
    sleep(1.0)


# How can we make this better?
