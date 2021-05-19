from threading import Thread


class Clip:
    def __init__(self, func, beat_offset):
        self.func = func
        self.beat_offset = beat_offset


class Track:
    def __init__(self, func, metronome, beat_offset=0):
        self.metronome = metronome
        self.enabled = False

        self.clip = Clip(func, beat_offset)

        self._thread = None

    def start_thread(self):
        self.stop_thread()
        self._thread = Thread(target=self.play_clip)
        self._thread.start()

    def stop_thread(self, timeout=0):
        if isinstance(self._thread, Thread) and self._thread.is_alive():
            self._thread.join(timeout)

    def enable(self):
        if not self.enabled:
            self.enabled = True
            self.start_thread()

    def disable(self):
        self.enabled = False
        self.stop_thread()

    def play_clip(self):
        self.metronome.wait_for_tick()
        self.metronome.beat_sleep(self.clip.beat_offset)

        while self.enabled:
            if callable(self.clip.func):
                self.clip.func(self.metronome)
