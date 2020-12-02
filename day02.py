#!/usr/bin/env python3

import re

# Sometimes I wish Boolean exclusive-or was a builtin in languages.
def xor(pred1, pred2):
    if pred1:
        if pred2:
            return False
        else:
            return True
    else:
        if pred2:
            return True
        else:
            return False

class PasswordPolicy:
    def __init__(self, minimum, maximum, letter):
        self.minimum = minimum
        self.maximum = maximum
        self.letter  = letter

class SledPasswordPolicy(PasswordPolicy):
    def valid(self, password):
        matches = password.count(self.letter)
        return self.minimum <= matches <= self.maximum

class TobogganPasswordPolicy(PasswordPolicy):
    def valid(self, password):
        positions = (password[self.minimum - 1], password[self.maximum - 1])
        return xor((positions[0] == self.letter), positions[1] == self.letter)

part1 = 0
part2 = 0
with open("data/day02.text") as data_file:
    for line in data_file:
        reader = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
        sled_policy = SledPasswordPolicy(int(reader[1]), int(reader[2]), reader[3])
        toboggan_policy = TobogganPasswordPolicy(int(reader[1]), int(reader[2]), reader[3])
        password = reader[4]

        if sled_policy.valid(password):
            part1 += 1
        if toboggan_policy.valid(password):
            part2 += 1

print("---")
print("day: 2")
print("part1: %d" % part1)
print("part2: %d" % part2)
