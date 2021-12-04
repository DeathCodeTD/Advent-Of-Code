#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as file:
    inputs = file.read().splitlines()

HORIZONTAL_POS = 0
DEPTH = 0
AIM = 0
FORWARDS = []
for i in range(len(inputs)):
    DIRECTION, VALUE = inputs[i].split()
    VALUE = int(VALUE)
    if DIRECTION == "forward":
        HORIZONTAL_POS += VALUE
        DEPTH = DEPTH + AIM * VALUE
    elif DIRECTION == "down":
        AIM += VALUE
    elif DIRECTION == "up":
        AIM -= VALUE
PRODUCT = HORIZONTAL_POS * DEPTH
print(PRODUCT)
