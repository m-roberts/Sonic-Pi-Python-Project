from sequencer.metronome import Metronome
from .track import Track
from psonic import in_thread


class Sequencer:
    def __init__(self, bpm=120, ticks_per_beat=4):
        self.metronome = Metronome(bpm, ticks_per_beat)

        self.trigger_events = dict()

        self.kick = Track("kick")
        self.snare = Track("snare")
        self.perc = Track("perc")
        self.sample = Track("sample")
        self.bass = Track("bass")
        self.lead = Track("lead")
        self.arp = Track("arp")
        self.chord = Track("chord")
        self.perform = Track("perform")

        # Perform is a 'hot' track
        self.perform.enable()

        self.all_tracks = [
            self.kick,
            self.snare,
            self.perc,
            self.sample,
            self.bass,
            self.lead,
            self.arp,
            self.chord,
            self.perform
        ]

    def start(self):
        while self.metronome.is_active:
            self.metronome.tick()

            print(self.metronome.tick_tuple)

            if self.metronome.tick_tuple in self.trigger_events:
                func = self.trigger_events[self.metronome.tick_tuple]
                if callable(func):
                    func()

            self.metronome.cue()
            self.metronome.tick_sleep()

    def enable_tracks(self, tracks_to_enable, exclusive=False):
        for t in self.all_tracks:
            if (isinstance(tracks_to_enable, list) and t in tracks_to_enable) or (t == tracks_to_enable):
                t.enable()
            elif exclusive:
                t.disable()

    def disable_tracks(self, tracks_to_disable, exclusive=False):
        for t in self.all_tracks:
            if (isinstance(tracks_to_disable, list) and t in tracks_to_disable) or (t == tracks_to_disable):
                t.disable()
            elif exclusive:
                t.enable()

    def stop(self):
        for t in self.all_tracks:
            t.disable()

    def register_event(self, func, bar, beat=1, tick=1):
        self.trigger_events[(bar, beat, tick)] = func

    def set_length(self, bars, beats=0, ticks=0):
        ticks_in_bars = (bars * self.metronome.beats_per_bar * self.metronome.ticks_per_beat)
        ticks_in_beats = (beats * self.metronome.ticks_per_beat)

        total_ticks = ticks_in_bars + ticks_in_beats + ticks + 1

        self.metronome.stop_at(total_ticks)
