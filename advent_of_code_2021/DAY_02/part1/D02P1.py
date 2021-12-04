#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as file:
    inputs = file.read().splitlines()

HORIZONTAL_POS = 0
DEPTH = 0

for i in range(len(inputs)):
    DIRECTION, VALUE = inputs[i].split()
    VALUE = int(VALUE)
    if DIRECTION == "forward":
        HORIZONTAL_POS += VALUE
    elif DIRECTION == "down":
        DEPTH += VALUE
    elif DIRECTION == "up":
        DEPTH -= VALUE
    print(f'{DIRECTION} {VALUE}: {HORIZONTAL_POS}, {DEPTH}')
PRODUCT = HORIZONTAL_POS * DEPTH
print(PRODUCT)
