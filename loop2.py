#!/usr/bin/env python

i = 0
while i <= 49:
    if i == 13:
        i += 1
        continue
    if i == 19:
        i += 1
        continue
    print i
    if i == 45:
        break
    i += 1
