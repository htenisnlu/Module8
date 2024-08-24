# Python Problem Set

This repository contains solutions to five basic Python programming problems. Each problem is designed to practice different programming concepts such as conditionals, loops, functions, and object-oriented programming.

## Problem 1: Check Equality of Two Inputs

**Function:** `check_equality()`

This function prompts the user to input two values and then checks whether they are equal. The result is printed to the console.

### Example Usage:
```python
check_equality()
```
- **Input:** Enter two values.
- **Output:** "The two inputs are equal." or "The two inputs are not equal."

## Problem 2: Check Sum Against 10

**Function:** `check_sum()`

This function prompts the user to input two numbers, computes their sum, and then checks if the sum is greater than, less than, or equal to 10. The result is printed to the console.

### Example Usage:
```python
check_sum()
```
- **Input:** Enter two numbers.
- **Output:** "The sum is greater than 10.", "The sum is less than 10.", or "The sum is equal to 10."

## Problem 3: Check if 5 is in the List

**Function:** `check_for_five(lst)`

This function takes a list as an argument and checks if the value 5 is in that list. The result is printed to the console.

### Example Usage:
```python
check_for_five([1, 2, 3, 5, 8])
```
- **Input:** A list of integers.
- **Output:** "The value 5 is in the list." or "The value 5 is not in the list."

## Problem 4: Check if a Year is a Leap Year

**Function:** `is_leap_year(year)`

This function takes a year as a parameter and returns `True` if the year is a leap year, otherwise it returns `False`.

### Example Usage:
```python
is_leap_year(2020)
```
- **Input:** A year (integer).
- **Output:** `True` if the year is a leap year, `False` otherwise.

### Leap Year Rules:
- The year is evenly divisible by 4.
- If the year is evenly divisible by 100, it is not a leap year unless it is also divisible by 400.

## Problem 5: Game Character Task Check

**Class:** `Character`

This class represents a game character with a nickname, a list of weapons, and a list of weaknesses. The `check_tasks` method checks whether the character can perform certain tasks based on their items and weaknesses.

### Tasks:
1. **Climb a mountain** - Requires `rope`, `coat`, `first aid kit`, and cannot have the `slow` debuff.
2. **Cook a meal** - Requires `pan`, `groceries`, and cannot have the `slow` debuff.
3. **Write a book** - Requires `pen`, `paper`, `idea`, and cannot have the `confusion` debuff.

### Example Usage:
```python
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])
player1.check_tasks()
```
- **Output:** 
  - Whether the character can perform each task based on the items they have and their debuffs.

---

## Requirements

- Python 3.x

## How to Run

1. Clone the repository.
2. Open the terminal and navigate to the project directory.
3. Run each function by importing the module or using the Python interpreter.
