#!/usr/bin/env python
# -*- coding: utf-8 -*-
# weird solution ahead but trust me i did it for a reason which this file isn't big enough to write
with open('input.txt', 'r') as file:
    inputs = file.read().splitlines()

REJECTED_INDEXES = []
REJECTED_NUMBERS = []

while len(inputs) > 1:

    for INDEX in range(len(inputs[0])):
        ZEROS = 0
        ONES = 0
        for BINS in inputs:
            if BINS[INDEX] == "0":
                ZEROS += 1
            else:
                ONES += 1

        if ZEROS > ONES and len(inputs) > 1:
            for i, BIN in enumerate(inputs):
                if BIN[INDEX] == "1":
                    REJECTED_INDEXES.append(i)
            for INDEXES in REJECTED_INDEXES:
                REJECTED_NUMBERS.append(inputs[INDEXES])
            for NUMBERS in REJECTED_NUMBERS:
                inputs.remove(NUMBERS)
            REJECTED_INDEXES = []
            REJECTED_NUMBERS = []

        elif ZEROS < ONES and len(inputs) > 1:
            for i, BIN in enumerate(inputs):
                if BIN[INDEX] == "0":
                    REJECTED_INDEXES.append(i)
            for INDEXES in REJECTED_INDEXES:
                REJECTED_NUMBERS.append(inputs[INDEXES])
            for NUMBERS in REJECTED_NUMBERS:
                inputs.remove(NUMBERS)
            REJECTED_INDEXES = []
            REJECTED_NUMBERS = []

        elif ZEROS == ONES and len(inputs) > 1:
            for i, BIN in enumerate(inputs):
                if BIN[INDEX] == "0":
                    REJECTED_INDEXES.append(i)
            for INDEXES in REJECTED_INDEXES:
                REJECTED_NUMBERS.append(inputs[INDEXES])
            for NUMBERS in REJECTED_NUMBERS:
                inputs.remove(NUMBERS)
            REJECTED_INDEXES = []
            REJECTED_NUMBERS = []

OXYGEN = inputs[0]
OXYGEN_RATE = int(OXYGEN, 2)

with open('input.txt', 'r') as file:
    inputs = file.read().splitlines()

REJECTED_INDEXES = []
REJECTED_NUMBERS = []

while len(inputs) > 1:

    for INDEX in range(len(inputs[0])):
        ZEROS = 0
        ONES = 0
        for BINS in inputs:
            if BINS[INDEX] == "0":
                ZEROS += 1
            else:
                ONES += 1

        if ZEROS > ONES and len(inputs) > 1:
            for i, BIN in enumerate(inputs):
                if BIN[INDEX] == "0":
                    REJECTED_INDEXES.append(i)
            for INDEXES in REJECTED_INDEXES:
                REJECTED_NUMBERS.append(inputs[INDEXES])
            for NUMBERS in REJECTED_NUMBERS:
                inputs.remove(NUMBERS)
            REJECTED_INDEXES = []
            REJECTED_NUMBERS = []

        elif ZEROS < ONES and len(inputs) > 1:
            for i, BIN in enumerate(inputs):
                if BIN[INDEX] == "1":
                    REJECTED_INDEXES.append(i)
            for INDEXES in REJECTED_INDEXES:
                REJECTED_NUMBERS.append(inputs[INDEXES])
            for NUMBERS in REJECTED_NUMBERS:
                inputs.remove(NUMBERS)
            REJECTED_INDEXES = []
            REJECTED_NUMBERS = []

        elif ZEROS == ONES and len(inputs) > 1:
            for i, BIN in enumerate(inputs):
                if BIN[INDEX] == "1":
                    REJECTED_INDEXES.append(i)
            for INDEXES in REJECTED_INDEXES:
                REJECTED_NUMBERS.append(inputs[INDEXES])
            for NUMBERS in REJECTED_NUMBERS:
                inputs.remove(NUMBERS)
            REJECTED_INDEXES = []
            REJECTED_NUMBERS = []

CO2 = inputs[0]
CO2_RATE = int(CO2, 2)

FINAL_NUM = CO2_RATE * OXYGEN_RATE
print(FINAL_NUM)
