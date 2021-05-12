# Sonic Pi Python Project

`run.py`: Initializes sequencer, enables tracks, starts sequencer

`Sequencer` provides an easy way to access playing `Track`s.
`Track`s can be enabled/disabled, and have a background thread that will start trying to play a clip in a loop.
`Metronome` is a Singleton that tracks the number of beat 'ticks', so that clips being played by tracks know when to trigger samples and notes.

`clips.py` contains the functions for each `Track`'s default clip behaviour.

### TODO
* track waits until sequencer starts to start playing a clip
* allow easy override of functions
* allow enable/disable multiple tracks at once
* evaluate grouping tracks, such as drums (e.g. seq.drums.disable)
