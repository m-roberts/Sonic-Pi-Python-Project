from threading import Thread


class Track:
    def __init__(self, func, metronome):
        self.metronome = metronome
        self.enabled = False

        self.func = func

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

        while self.enabled:
            if callable(self.clip.func):
                self.clip.func(self.metronome)
