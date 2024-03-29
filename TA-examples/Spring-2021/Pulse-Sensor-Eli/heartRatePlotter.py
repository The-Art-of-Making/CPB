#Edited Spring 2022 by Eli Wissenbach.#
#Uses the onboard neopixel and a buzzer to measure heart rate with noise reduction#

import time

import analogio
import board
import neopixel
from adafruit_circuitplayground import cp
def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0



# Turn only pixel #1 green
cp.pixels[1] = (0, 255, 0,1)

# How many light readings per sample
NUM_OVERSAMPLE = 10
# How many samples we take to calculate 'average'
NUM_SAMPLES = 20
samples = [0] * NUM_SAMPLES
lasttime = time.monotonic()

while True:
    for i in range(NUM_SAMPLES):
        # Take NUM_OVERSAMPLE number of readings really fast
        oversample = 0
        for s in range(NUM_OVERSAMPLE):
            oversample += float(cp.light)
        # and save the average from the oversamples
        samples[i] = oversample / NUM_OVERSAMPLE  # Find the average

        mean = sum(samples) / float(len(samples))  # take the average
        print((samples[i] - mean,))  # 'center' the reading

        if i > 0:
            # If the sign of the data has changed munus to plus
            # we have one full waveform (2 zero crossings), pulse LED
            if sign(samples[i]-mean) <= 0 and sign(samples[i-1]-mean) > 0:
                cp.pixels[9] = (200, 0, 0)  # Pulse LED
                cp.play_tone(262,.5)
            else:
                cp.pixels[9] = (0, 0, 0)    # Turn LED off

        time.sleep(0.025)  # change to go faster/slower
# Write your code here :-)
