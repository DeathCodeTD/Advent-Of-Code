#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as file:
    inputs = file.read().splitlines()
GAMMA_BIN = ""
EPLISION_RATE = ""
for DIGIT in range(12):
    ZEROS = 0
    ONES = 0
    for BIN_NUMBER in inputs:
        if BIN_NUMBER[DIGIT] == "0":
            ZEROS += 1
        else:
            ONES += 1
    if ZEROS > ONES:
        GAMMA_BIN = GAMMA_BIN + "0"
        EPLISION_RATE = EPLISION_RATE + "1"
    else:
        GAMMA_BIN = GAMMA_BIN + "1"
        EPLISION_RATE = EPLISION_RATE + "0"
#alternatively can get the eplision rate by changing the 0s to 1s and 1s to 0s from the GAMMA_RATE
GAMMA_RATE = int(GAMMA_BIN, 2)
EPLISION_RATE = int(EPLISION_RATE, 2)

print(GAMMA_RATE * EPLISION_RATE)
