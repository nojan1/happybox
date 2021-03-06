# Change this line to import the correct implementation
from implementation_file import Implementation

##### No need to change anything below ######
from button import Button

import time
import board
import neopixel
import digitalio

NUM_PIXELS = 64
STEP_DELAY = 0.1
ALL_GOOD_CHECK_DELAY = 60

buttons = [Button(x) for x in [board.D17, board.D22, board.D27, board.D24]]

logo = digitalio.DigitalInOut(board.D23)
logo.direction = digitalio.Direction.OUTPUT
logo.value = True

implentation = Implementation()

pixels = neopixel.NeoPixel(
    board.D18, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

factors = [1, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50, 0.45]
baseColors = [(0, 255, 0), (255, 200, 0), (255, 50, 0), (255, 0, 0)]
lastStep = 0
offset = 0
offsetDirection = 1

lastAllGoodCheck = 0
allGood = False

def onImplementationError():
    global allGood
    allGood = False


def ledAnimationCycle():
    global pixels, baseColors, factors, STEP_DELAY, NUM_PIXELS, offset, offsetDirection, lastStep

    if time.time() - lastStep > STEP_DELAY:
        for i in range(NUM_PIXELS):
            red = baseColors[i // 16][0] * factors[offset]
            green = baseColors[i // 16][1] * factors[offset]
            blue = baseColors[i // 16][2] * factors[offset]

            pixels[i] = (int(red), int(green), int(blue))

        pixels.show()
        lastStep = time.time()

        offset += offsetDirection

        if offset == len(factors) - 1:
            offsetDirection = -1
        elif offset == 0:
            offsetDirection = +1


def buttonPressAnimation(buttonNumber):
    global pixels, baseColors
    pixels.fill((0, 0, 0))

    for i in range(2):
        for i in range(8):
            pixels[i + (buttonNumber * 16)] = baseColors[buttonNumber]
            pixels[i + 8 + (buttonNumber * 16)] = baseColors[buttonNumber]
            pixels.show()

            time.sleep(0.015)

        for i in range(8):
            pixels[i + (buttonNumber * 16)] = (0, 0, 0)
            pixels[i + 8 + (buttonNumber * 16)] = (0, 0, 0)
            pixels.show()

            time.sleep(0.015)


def checkButtons():
    global buttons, implentation
    for i, button in enumerate(buttons):
        if button.IsPressed():
            print("Button " + str(i) + " is pressed")
            implentation.HandleValue(i, onImplementationError)
            buttonPressAnimation(i)


def checkAllGood():
    global lastAllGoodCheck, implentation, allGood 
    if time.time() - lastAllGoodCheck > ALL_GOOD_CHECK_DELAY:
        allGood = implentation.AllGood()
        lastAllGoodCheck = time.time()


def main():
    global pixels, logo

    pixels.fill((0, 0, 0))
    pixels.show()

    while True:
        checkAllGood()

        if allGood:
            logo.value = True

            ledAnimationCycle()
            checkButtons()
            time.sleep(0.002)
        else:
            logo.value = not logo.value
            time.sleep(0.1)


if __name__ == "__main__":
    main()
