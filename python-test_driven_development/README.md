# Python - Test Driven Development

This project focuses on the implementation of Test-Driven Development (TDD) in Python. It covers creating robust functions through input validation and documenting/testing those functions using `doctest` and `unittest`.

## Requirements
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- Code must follow `pycodestyle` (version 2.8.*)
- All modules, classes, and functions must have documentation (`__doc__`)

## Files and Tasks

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Integers addition** | `0-add_integer.py` | Function that adds 2 integers/floats. Includes TDD with `tests/0-add_integer.txt`. |
| **1. Divide a matrix** | `2-matrix_divided.py` | Divides all elements of a matrix by a divisor. Includes `tests/2-matrix_divided.txt`. |
| **2. Say my name** | `3-say_my_name.py` | Prints "My name is <first name> <last name>". Includes `tests/3-say_my_name.txt`. |
| **3. Print square** | `4-print_square.py` | Prints a square with the character `#`. Includes `tests/4-print_square.txt`. |
| **4. Text indentation** | `5-text_indentation.py` | Prints text with 2 new lines after `.`, `?`, and `:`. Includes `tests/5-text_indentation.txt`. |
| **5. Max integer** | `tests/6-max_integer_test.py` | Unittests for an existing `max_integer` function using the `unittest` module. |

## How to Run Tests
- **Doctests:** `python3 -m doctest -v ./tests/<test_file>.txt`
- **Unittests:** `python3 -m unittest tests.6-max_integer_test`
