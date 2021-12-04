#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as file:
    inputs = file.readlines()
INCRIMENTS = 0
for i in range(len(inputs)):
    a = inputs[i]
    if i + 1 >= len(inputs):
        break
    b = inputs[i + 1]
    if b > a:
        INCRIMENTS += 1

print(INCRIMENTS)
