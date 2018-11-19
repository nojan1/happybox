import digitalio
import time

DEBOUNCE_TIME = 0.05

class Button(object):
    def __init__(self, pin):
        self.button = digitalio.DigitalInOut(pin)
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.UP

        self.timeDown = None
        self.inhibit = False

    def IsPressed(self):
        if not self.button.value:
            if self.timeDown == None:
                self.timeDown = time.time()
            elif time.time() - self.timeDown >= DEBOUNCE_TIME and not self.inhibit:
                self.inhibit = True
                return True
        else:
            self.inhibit = False
            self.timeDown = None

        return False

