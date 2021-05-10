from .sequencer import Sequencer


seq = Sequencer()

# Enable tracks
seq.kick.enable()
seq.snare.enable()
seq.perc.enable()
seq.sample.enable()
seq.bass.enable()
seq.lead.enable()
seq.arp.enable()
seq.chord.enable()

# Start sequencer
seq.start()
