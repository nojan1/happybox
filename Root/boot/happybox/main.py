import time
import board
import neopixel
import digitalio

def setupButton(pin):
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN

    return button

buttons = [setupButton(x) for x in [board.D17, board.D22, board.D27, board.D23]]

logoLight = 00
GPIO.setup(logoLight, GPIO.OUT)
GPIO.output(logoLight, 1)

logo = digitalio.DigitalInOut(board.D23)
logo.direction = digitalio.Direction.output
logo.value = True

pixels = neopixel.NeoPixel(board.D18, 64, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

while True:
    pass