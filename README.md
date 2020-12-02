# Advent20.py

My version of [2020's Advent of Code](https://adventofcode.com/2020).
May as well take this time to learn some Python as I never... Well...
I never really took the time to learn it before.
This time of year's as good as any to learn something new.

# Tasks

## [1. Report Repair][1]

[1]: https://adventofcode.com/2020/day/1

Literally my first Python program ever.
Coming from a Ruby and Lisp background, it took a lot of understanding
how the Pythonic mindset works before coming to the conclusion (read:
being told repeatedly) that Python is not Lisp and trying to map and
reduce and such with crazy high-order functions will only end in tears.

Many tears were shed after finding out multi-line lambdas are "discouraged".

## [2. Password Philosophy][2]

[2]: https://adventofcode.com/2020/day/2

It's high time I dug a bit into classes and objects.
Classes are not quite a pleasant experience here in Python compared to
Ruby where they were first-class citizens (pun not intended).
Reading through the [random remarks](https://docs.python.org/3.8/tutorial/classes.html#random-remarks),
it turns out that classes are basically plain-old-Python-objects
(POPOs) with no real way to properly hide data.

Also, what the heck is up with `sum()`?
I found out the hard way that it counts Booleans too.
Sounds like one could just `map()` a predicate function on an iterable
and sum them up that way.
Up in Rubyland we have [`Enumerable#count`][rb:count] to count truthy values.

```python
sum((True, True, False, True, False, False)) # => 3
```

[rb:count]: https://ruby-doc.org/core-2.7.1/Enumerable.html#method-i-count

# Consensus

To compare my Ruby upbringing with this Pythonic way to do things,
can't say I'm too fond of Python.
Usable with time?  Yes.
Easy to learn?  No.
In fact the prime difference between the two languages is that Ruby is
much more focused on object-orientation and Python is meant to be
something like a simpler C.

With Ruby, everything is an object with methods and proper mechanisms
to tuck attributes out of sight.
The most difficult thing to grasp in it may be blocks.
If you played with the Lisp family of programming languages, you
suddenly realize blocks are just lambda functions.
