# Behavior, Strategy, Implementation

A quick introduction to 3 aspects of 1 function.

## Behavior

What does the function do? What are it’s arguments and it’s return value? How could you use it in a program? Behavior is all about what your function looks like "from the outside", without caring about what is written inside the body.

Functions behavior is generally described using **documentation**, **unit tests** and **use cases**:

<details>
<summary><strong>Documentation (docstring comment)</strong></summary>

```python
"""generates a list containing the first n numbers of the fibonacci sequence

Parameters:
  n: int, greater than or equal to zero

Returns -> list[int] with the first n numbers of the fibonacci sequence

>>> fib_list(0)
[]

>>> fib_list(4)
[0, 1, 1, 2]

>>> fib_list(8)
[0, 1, 1, 2, 3, 5, 8, 13]
"""
```

</details>

<details>
<summary><strong>Unit Tests (pass/fail assertions)</strong></summary>

```python
import unittest

from fib_list import fib_list


class TestFibLib(unittest.TestCase):
    """Test the fib_lib function"""

    def test_0(self):
        """It should evaluate 0 to []"""
        self.assertEqual(fib_list(0), [])

    def test_1(self):
        """It should evaluate 1 to [0]"""
        self.assertEqual(fib_list(1), [0])

    def test_2(self):
        """It should evaluate 2 to [0, 1]"""
        self.assertEqual(fib_list(2), [0, 1])

    def test_3(self):
        """It should evaluate 3 to [0, 1, 1]"""
        self.assertEqual(fib_list(3), [0, 1, 1])

    def test_4(self):
        """It should evaluate 4 to [0, 1, 1, 2]"""
        self.assertEqual(fib_list(4), [0, 1, 1, 2])

    def test_5(self):
        """It should evaluate 5 to [0, 1, 1, 2, 3]"""
        self.assertEqual(fib_list(5), [0, 1, 1, 2, 3])

    def test_9(self):
        """It should evaluate 9 to [0, 1, 1, 2, 3, 5, 8, 13, 21]"""
        self.assertEqual(fib_list(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_less_than_0(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            fib_list(-1)

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            fib_list(1.0)


if __name__ == "__main__":
    unittest.main()
```

</details>

<details>
<summary><strong>Use Cases ("real-world" examples)</strong></summary>

```python
from fib_list import fib_list

# %% what about big numbers?

print(fib_list(150))


# %% does the function return the same or different arrays?

array_1 = fib_list(3)
array_2 = fib_list(3)

# the function returned two different arrays with the same values
assert array_1 == array_2, "the arrays store the same values"
assert array_1 is not array_2, "the variables do not reference the same array"
```

</details>

## Strategy

How do you approach solving the problem? There are many strategies to solve the same problem! A way to practice strategy is to think of transforming the arguments to the return value in small steps, _focusing on the data not the code_. This is the realm of flow charts, diagrams, and pseudo-code.

One way to approach strategy is to solve the problem a few different ways by hand, writing what you expect to change in memory at each step. Like if you were the debugger and you couldn't see the source code. Using a pencil and paper is a the best way to go, pick a few test cases and see how you'd solve them manually.

Variable names and comments are useful tools for explaining your function's strategy.

## Implementation

Which language features and which lines of code did you use to write the code for your strategy? There are many ways to implement the same strategy!
