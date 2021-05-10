from looper.sequencer import Sequencer

seq = Sequencer(bpm=120)

seq.kick.enable()
seq.snare.enable()
seq.perc.enable()
seq.hiss.enable()
seq.bass.enable()
seq.lead.enable()
seq.arp.enable()
seq.chord.enable()

seq.start()
