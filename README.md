# Documenting and Testing

In 6.00.1x you have learned about python, algorithms, debugging and testing, all as individual study. This is necessary for building your foundations, but data science is a social activity. In the Documenting and Testing workshop we will expand on what you have learned in 6.00.1x by introducing some techniques that will help you understand code written by others, and help you write code that others can easily read, understand and trust.

- [Learning Objectives](#learning-objectives)
- [Prep Work](#prep-work)
- [Workshop Outline](#workshop-outline)

---

## Learning Objectives

<details><summary>Priorities: 🥚🐣🐥🐔 (click for more info)</summary>
<br />

Learning objective for this workshop are labeled so you can prioritize your study time. The emojis show the _minimum_ mastery you are expected to achieve for each skill, but there is no maximum! If you have the time you should aim to master all of the skills introduced in this workshop.

- 🥚 You are expected to master these skills. They are the foundations you will need to move forward.
- 🐣 You are expected to be comfortable with these skills. It's ok if you still need help sometimes.
- 🐥 You are expected to be familiar with these skills. It's enough to recognize them in practice and apply them with help.
- 🐔 You are not expected to know these skills, but they are important if you want to excel. You should only focus on these after mastering the 🥚, 🐣 and 🐥 objectives.

---

</details>

### Function Documentation

- 🥚 You can read docstrings to understand a function's _behavior_.
- 🥚 You can import a module to the console and use `help(<function>)` to read it's docstring.
- 🥚 You can distinguish between a function's **_behavior_**, **_strategy_** and **_implementation_**.
- 🥚 You can write a clear and complete _docstring_ to describe a function's _behavior_.
- 🥚 You can write 2-3 _doctests_ to informally demonstrate a function's _behavior_. (white space matters in a docstring test case!)

### Function Implementation

- 🥚 You can use a _formatter_ and _linter_ to write code that follows community conventions.
- 🥚 You can read and write type annotations to describe a function's _type signature_.
- 🥚 You can write a clear and helpful name for a function, and use the same name for the file.
- 🥚 You can write assertions in a function for _defensive programming_.
- 🐣 You can write _self-documenting code_ that uses variable names and comments to explain a function's **_strategy_**.

### Function Testing

- 🥚 You can use a sandbox file to informally explore a function's _behavior_.
- 🥚 You can read and run unit tests to understand a function's _behavior_.
- 🥚 You can import a module in your console and run its doctest.
- 🥚 You can write a simple suite of unit tests with some boundary cases.
- 🐣 You can write a full suite of unit tests including comprehensive boundary cases, assertions checks, and glass box tests.

---

# Prep Work

Things to prepare before the workshop:

- Download this repository to your computer. You can use git if you know how, otherwise you can just [download the code directly](https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github/).
- Download [Spyder](https://docs.spyder-ide.org/current/installation.html), the IDE recommended by 6.00.1x.
  - If you use a different IDE, not a problem! Install Black (Python formatter) and Pylint (Python linter).
  - If you are not able install an IDE, you can still follow along with your group.

---

## Workshop Outline

### Workshop Overview _(all together)_

> ~10 minutes

The workshop instructor will introduce the main concepts of this workshop:

- Introduce the workshop's [learning objectives](#learning-objectives).
- Discuss the difference between a function's [behavior, strategy and implementation](./behavior-strategy-implementation.md).

### Behavior, Strategy, Implementation _(small groups)_

> ~15 minutes

Explore and discuss the examples in [behavior, strategy and implementation](./behavior-strategy-implementation.md).

### Introduce the Exercises _(all together)_

> ~15 minutes

- Each group will have 1 minute to share:
  - One thing they couldn't understand
  - One interesting thing they learned
- Discuss why documenting and testing important.
- The instructor does a guided walk through the `/examples` folder, reading and running each file:
  - `<module_name>.py`, `test_<module_name>.py`, `<module_name>_sandbox.py`
  - How to study and run each file
  - Demonstrate how to use the [Code Review Checklist](./code-review-checklists.md)
  - Demonstrate use the console to read docstrings and run doctests
- Introduce the group exercise

### Document and Test the Mystery Functions _(small groups)_

> ~30 minutes

You will work on the `/exercises` in small groups. You are not expected to finish all of the exercises during the workshop, you may not even finish all of the steps for one mystery function. That's ok! There are extra exercises so you can keept practicing after the workshop.

Study one mystery function at a time following these steps:

1. Explore the mystery function using `<module_name>_sandbox.py`. :
   - There are no wrong answers! Try passing all sorts of arguments until you think you understand the function's _behavior_.
2. Describe the function's behavior in `<module_name>.py`:
   - Give the function a descriptive name and rename the files to match.
   - Write type annotations for the function
   - Write a first draft docstring, you can always update it later
3. Write black box unit tests for the function in `test_<module_name>.py`:
   - Ask yourself: _How can I break my program?_
   - Write as many boundary cases as you can
4. Study the function's code to understand its strategy:
   1. Change the variable names to something helpful
   1. Write comments when necessary to explain the function's strategy
5. Take your code to the next level:
   1. Write clear and helpful assertions in the function
   1. Write unit tests for your assertions
   1. Write glass box tests for the function's implementation

### Discussion _(all together)_

> ~20 minutes

Back together, you will have an informal discussion with the other groups and the workshop leader.

1. Each group will have 2-3 minutes to share:
   - One thing they couldn't figure out
   - One surprising thing they learned
   - One thing they'd like to discuss with the full class
2. Discuss!
