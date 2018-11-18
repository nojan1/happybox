from implementation_file import Implementation

import time
import board
import neopixel
import digitalio

from button import Button

buttons = [Button(x) for x in [board.D17, board.D27, board.D22, board.D24]]

logo = digitalio.DigitalInOut(board.D23)
logo.direction = digitalio.Direction.OUTPUT
logo.value = True

implentation = Implementation()

pixels = neopixel.NeoPixel(
    board.D18, 64, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

ledBuffer = [(0, 0, 0)) for x in range(64)]
pixels.fill((0, 0, 0))
pixels.show()

while True:
    # Update led animation

    for i, button in enumerate(buttons):
        if button.IsPressed():
            implentation.HandleValue(i, lambda _: pass)

            pixels.fill((0, 0, 0))
            pixels.show()

            break
