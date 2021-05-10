from psonic import *
from math import sin, radians
from .clips import *

def sync_and_loop(func):
    """Metronome decorator"""

    def wrapper():
        metronome.sync()
        while True:
            func()

    return wrapper

@in_thread
@sync_and_loop
def kick_drum_track():
    kick_drum()

@in_thread
@sync_and_loop
def hi_hat_track():
    hi_hat()
 
@in_thread
@sync_and_loop
def snare_track():
    snare()

@in_thread
@sync_and_loop
def vinyl_hiss_track():
    vinyl_hiss()

@in_thread
@sync_and_loop
def synth_wub_track():
    synth_wub

@in_thread
@sync_and_loop
def synth_plucks_track():
    synth_plucks()
