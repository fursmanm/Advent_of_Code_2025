# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 14:38:21 2025

@author: Fursman
"""

import re

def zeroes (lines):
    pos = 50
    count = 0
    turn = re.compile(r'^([LR])([0-9]+)$')

    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue

        m = turn.match(line)
        if not m:
            raise ValueError(f"Invalid input on line {i}: {line!r}")

        dir_, dist = m.group(1), int(m.group(2))

        # Move one click at a time to detect passes over 0
        for _ in range(dist):
            if dir_ == "L":
                pos = (pos - 1) % 100
            else:
                pos = (pos + 1) % 100

            if pos == 0:
                count += 1

    return count

with open(r"C:\Users\...\dial.txt", "r") as f:
    lines = f.readlines()

print(zeroes(lines))
