from implementation_base import ImplementationBase

class Implementation(ImplementationBase):
    def AllGood(self):
        return True

    def HandleValue(self, buttonNumber, errorDetected):
        #buttonNumber: 1 - 4
        #errorDetected: callback method to call if things start going wrong