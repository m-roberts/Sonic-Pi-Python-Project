play 70


# Each number represents the length of that section of ADSR in beats
play 70, release: 1
play 60, release: 2
play 60, release: 0.2


play 60, attack: 2
sleep 3
play 65, attack: 0.5


play 60, attack: 0.7, release: 4


play 60, attack: 4, release: 0.7


play 60, attack: 0.5, release: 0.5


play 60, attack: 0.3, sustain: 1, release: 1


play 60, attack: 0.1, attack_level: 1, decay: 0.2, sustain_level: 0.4, sustain: 1, release: 0.5


play 60, attack: 0.1, attack_level: 1, decay: 0.2, decay_level: 0.3, sustain: 1, sustain_level: 0.4, release: 0.5


# Play with these parameters with hardware
while True:
    play(C3, attack=sensor.value)
    sleep(0.5)
    play(C3, attack=sensor.value)
    sleep(0.5)
    play(G3, attack=sensor.value)
    sleep(0.5)
    play(G3, attack=sensor.value)
    sleep(0.5)
    play(A3, decay=sensor.value)
    sleep(0.5)
    play(A3, decay=sensor.value)
    sleep(0.5)
    play(G3, decay=sensor.value)
    sleep(1.0)

    play(F3, sustain=sensor.value)
    sleep(0.5)
    play(F3, sustain=sensor.value)
    sleep(0.5)
    play(E3, sustain=sensor.value)
    sleep(0.5)
    play(E3, sustain=sensor.value)
    sleep(0.5)
    play(D3, release=sensor.value)
    sleep(0.5)
    play(D3, release=sensor.value)
    sleep(0.5)
    play(C3, release=sensor.value)
    sleep(1.0)
