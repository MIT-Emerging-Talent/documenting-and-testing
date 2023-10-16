#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A file for experimenting with different fibonacci_list use cases
"""

from fibonacci_list import fibonacci_list

# %% what about big numbers?

print(fibonacci_list(150))

# %% is it really a Fibonacci sequence?

huge_list = fibonacci_list(500)

for index in range(2, 500):
    two_back = huge_list[index - 2]
    one_back = huge_list[index - 1]
    current = huge_list[index]

    assert two_back + one_back == current, f"entry {index} is not correct"

# %% does the function return the same or different arrays?

array_1 = fibonacci_list(4)
array_2 = fibonacci_list(6)

# the function returned two different arrays with the same values
assert array_1 == array_2, "the arrays store the same values"
assert array_1 is not array_2, "the variables do not reference the same array"
