#!/usr/bin/env python3

from itertools import combinations
from math import prod

# We're *LITERALLY* talking about a guy's first Python program,
# cut him some slack!
# ...He's just used to doing higher-order styles from Lisp and a bit
# of Ruby, that's all.

input_file = open("data/day01.text", "r")
entries = list()

for entry in input_file:
    entries.append(int(entry))

def check_ledger(ledger, size):
    for entry in combinations(ledger, size):
        if sum(entry) == 2020:
            return prod(entry)

def part1():
    return check_ledger(entries, 2)

def part2():
    return check_ledger(entries, 3)

print(part1())
print(part2())
