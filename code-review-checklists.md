# Code Review Checklists

Writing a good function involves a lot of detail, way to much to remember right away! These checklists can help you review your own or your own classmates' code until the details become a habit.

## File Names

- [ ] The file names match the function

## Function Docstring

- [ ] behavior description
- [ ] parameter description
- [ ] return value description
- [ ] include any assumptions
- [ ] include 3 or more doctests
- [ ] include 1-2 use cases (if necessary)

## Function Implementation

- [ ] The code is auto-formatted
- [ ] The code has no (reasonable) linting mistakes
- [ ] Variables are named with snake_case
- [ ] The function has a clear and helpful name
- [ ] The file's name matches the function name
- [ ] The code follows the strategy as simply as possible
- [ ] Variable names are clear and helpful
- [ ] Comments explain the strategy (if necessary)
- [ ] There are type annotations
- [ ] (challenge) The code includes defensive assertions

## Unit Test Suite

- [ ] The test class has a helpful name in PascalCase
- [ ] The test class has a docstring
- Each unit test has
  - [ ] A helpful name
  - [ ] A clear docstring
  - [ ] Only one assertion
- [ ] All tests pass
- [ ] (challenge) Tests for defensive assertions
- [ ] (challenge) Tests for many boundary cases
- [ ] (challenge) Includes black-box and glass-box tests

## Files

- [ ] The file names match the function
- [ ] Module header in each file
- [ ] Module docstring in each file
