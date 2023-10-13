#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A file for experimenting with different fibonacci_list use cases
"""

from fibonacci_list import fibonacci_list

# %% what about big numbers?

print(fibonacci_list(150))


# %% does the function return the same or different arrays?

array_1 = fibonacci_list(4)
array_2 = fibonacci_list(6)

# the function returned two different arrays with the same values
assert array_1 == array_2, "the arrays store the same values"
assert array_1 is not array_2, "the variables do not reference the same array"
