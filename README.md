# My Progress in Python – Namami

A collection of (selected) beginner-friendly Python practice programs I solved during my IIT Madras Diploma. It covers the core building blocks of the language: **conditionals, loops, nested loops, and functions**. Each program solves one small, clearly stated problem, and several problems are solved in **more than one way** so the approaches can be compared side by side.


## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [What's Inside](#whats-inside)
  - [1. If, Else and Elif Conditions](#1-if-else-and-elif-conditions)
  - [2. While Loop](#2-while-loop)
  - [3. Difference Between While and For Loop](#3-difference-between-while-and-for-loop)
  - [4. Nested Loops](#4-nested-loops)
  - [5. Functions in Python](#5-functions-in-python)
- [Sample Dataset: Scores.csv](#sample-dataset-scorescsv)
- [Concepts Practiced](#concepts-practiced)
- [Conventions Used in This Repo](#conventions-used-in-this-repo)

---

## Project Structure

```
python-work-namami/
├── if, else and else-if (elif) conditions/
│   ├── P1.py
│   ├── P2.py
│   ├── P3_1.py
│   ├── P3_2.py
│   └── P4.py
├── while loop/
│   ├── P1.py
│   ├── P2.py
│   ├── P3.py
│   └── P4.py
├── difference between while and for loop/
│   ├── P1.py
│   ├── P2.py
│   ├── P3.py
│   └── P4.py
├── nested loops/
│   ├── P1.py
│   ├── P2.py
│   ├── P3.py
│   └── P4.py
├── functions in Python/
│   ├── P1.py
│   ├── P2_1.py
│   ├── P2_2.py
│   ├── P3_1.py
│   └── P3_2.py
└── Scores.csv
```


## Getting Started

### Prerequisites

- **Python 3.6 or newer** (the programs use f-strings)
- No third-party packages are required. Everything uses the standard library only.

### Running a Program

Each script is standalone and interactive: it asks for input in the terminal and prints the result.

```bash
# Clone or unzip the project, then move into it
cd python-work-namami

# Run any script by quoting the folder name (folder names contain spaces)
python "while loop/P1.py"
python "functions in Python/P2_2.py"
```

> **Note:** Because the folder names contain spaces and commas, always wrap the path in quotes.

---

## What's Inside

### 1. If, Else and Elif Conditions

Folder: `if, else and else-if (elif) conditions/`

| File | Problem |
| --- | --- |
| `P1.py` | Check whether a number is even or odd |
| `P2.py` | Check whether a number ends with 0, 5, or something else |
| `P3_1.py` | Assign a grade (A to E) from marks 0 to 100, using separate `if` blocks |
| `P3_2.py` | Same grading problem, using an `if-elif-else` chain |
| `P4.py` | Convert a flowchart into code: choose between train, coach, daytime flight or red-eye flight from travel time and price |

**Takeaway:** `P3_1.py` vs `P3_2.py` shows how `elif` removes redundant range checks and makes the conditions mutually exclusive.

### 2. While Loop

Folder: `while loop/`

| File | Problem |
| --- | --- |
| `P1.py` | Find the factorial of a number |
| `P2.py` | Count the number of digits in a number |
| `P3.py` | Reverse the digits of a number (handles negatives) |
| `P4.py` | Check whether a number is a palindrome |

These solve the problems **arithmetically**, using `%` and `//` to peel off digits one at a time.

### 3. Difference Between While and For Loop

Folder: `difference between while and for loop/`

The same four problems as above, re-solved with `for` loops so the two loop styles can be compared directly.

| File | Problem | `for` loop approach |
| --- | --- | --- |
| `P1.py` | Factorial | `range(num, 1, -1)` counting down |
| `P2.py` | Number of digits | Iterate over the characters of `str(num)` |
| `P3.py` | Reverse digits | Prepend each character to a result string |
| `P4.py` | Palindrome check | Reverse the string, then compare with the original |

**Takeaway:** use `for` when you know what you're iterating over (a range or a sequence); use `while` when the loop depends on a condition that changes as the program runs.

### 4. Nested Loops

Folder: `nested loops/`

| File | Problem |
| --- | --- |
| `P1.py` | Print all prime numbers less than the entered number |
| `P2.py` | Compute total profit/loss per trader, with an unknown number of traders and transactions (enter `-1` as the ID to stop, `0` as the trade amount to finish a trader) |
| `P3.py` | Compute day-wise total rainfall for a given number of days (enter `-1` to finish a day) |
| `P4.py` | Find the length of the longest word from a list of entered words (enter `-1` to stop) |

Several of these use a **sentinel value** (`-1` or `0`) to signal the end of input.

### 5. Functions in Python

Folder: `functions in Python/`

| File | Problem |
| --- | --- |
| `P1.py` | Count upper-case letters, lower-case letters, total characters and words in a sentence |
| `P2_1.py` | Area and perimeter of a circle and rectangle (straightforward script, `PI = 22/7`) |
| `P2_2.py` | Same problem as a **menu-driven program** with nested menus (uses `math.pi`) |
| `P3_1.py` | Check whether three coordinates form a triangle, using the **distance** between points and the triangle inequality |
| `P3_2.py` | Same check, using the **slope** of the lines connecting the points |

---

## Sample Dataset: Scores.csv

A 30-row table of student marks in three subjects.

| Column | Description |
| --- | --- |
| `CardNo` | Unique student ID (0 to 29) |
| `Name` | Student name |
| `Gender` | `M` or `F` |
| `DateOfBirth` | Stored as an Excel serial date number (e.g. `44142`), not as a formatted date |
| `CityTown` | City or town of the student |
| `Mathematics` | Marks in Mathematics |
| `Physics` | Marks in Physics |
| `Chemistry` | Marks in Chemistry |
| `Total` | Sum of the three subject marks |

Quick look with pandas (`pip install pandas`):

```python
import pandas as pd

df = pd.read_csv("Scores.csv")
print(df.head())
print(df["Total"].describe())
```

To convert the Excel serial dates into real dates:

```python
df["DateOfBirth"] = pd.to_datetime(df["DateOfBirth"], unit="D", origin="1899-12-30")
```

---

## Concepts Practiced

- Taking user input and converting types (`input`, `int`, `float`)
- Conditional logic: `if`, `else`, `elif`, nested conditions, logical operators
- `while` loops, `for` loops, `range()`, `break`
- Nested loops and sentinel-controlled input
- Arithmetic operators, including modulus (`%`) and floor division (`//`)
- String iteration, slicing-free reversal, and palindromes
- Defining and calling functions, returning values, passing arguments
- Menu-driven programs
- Multiple ways of solving one problem
- String formatting with f-strings, `.format()` and `%`


## Conventions Used in This Repo

- **`P<n>.py`**: Problem number *n* within a topic. The problem statement is in the docstring on the first line of each file.
- **`P<n>_<k>.py`**: Approach *k* for problem *n*, used where a problem is solved in more than one way.



## Author

[**Namami Diwan**](https://github.com/just-hoop-it/Portfolio-Namami)

Feel free to fork this repository and try your own approaches to the same problems.
