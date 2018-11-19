from implementation_base import ImplementationBase

import datetime

class Implementation(ImplementationBase):
    def __init__(self):
        self.file = open("presses.txt", "w+")

    def AllGood(self):
        return True

    def HandleValue(self, buttonNumber, errorDetected):
        self.file.write(str(datetime.datetime.utcnow()) + " " + str(buttonNumber) + "\n")