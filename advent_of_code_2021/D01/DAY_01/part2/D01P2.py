#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as file:
    inputs = file.read().splitlines()
INCRIMENTS = 0
SUM_LIST = []
for i in range(len(inputs)):
    a = int(inputs[i])
    if i + 2 >= len(inputs):
        break
    b = int(inputs[i + 1])
    c = int(inputs[i + 2])
    SUM = a + b + c
    SUM_LIST.append(SUM)
    print(SUM_LIST)
    if i > 0:
        if SUM_LIST[1] > SUM_LIST[0]:
            INCRIMENTS += 1
        SUM_LIST.pop(0)
print(INCRIMENTS)
