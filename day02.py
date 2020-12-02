#!/usr/bin/env python3

import re

class PasswordPolicy:
    def __init__(self, minimum, maximum, letter):
        self.minimum = minimum
        self.maximum = maximum
        self.letter  = letter

    def valid(self, password):
        matches = password.count(self.letter)
        return self.minimum <= matches <= self.maximum 

class Password:
    def __init__(self, password, policy):
        self.password = password
        self.policy = policy

    def valid(self):
        return policy.valid(self.password)

part1 = 0

with open("data/day02.text") as data_file:
    for line in data_file:
        reader = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
        policy = PasswordPolicy(int(reader[1]), int(reader[2]), reader[3])
        password = Password(reader[4], policy)

        if password.valid():
            part1 += 1

print("---")
print("day: 2")
print("part1: %d" % part1)
