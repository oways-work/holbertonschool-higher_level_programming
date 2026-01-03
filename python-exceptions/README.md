# Python - Exceptions

This project focuses on understanding and handling errors and exceptions in Python. The goal is to learn how to use `try`, `except`, `finally`, and `raise` statements to manage execution flow and handle unexpected behavior gracefully without crashing the program.

## Requirements

* **OS:** Ubuntu 20.04 LTS
* * **Language:** Python 3.8.5
  * * **Style:** pycodestyle (version 2.8.*)
    * * All files are executable
      * * All files end with a new line
        * * The first line of all files is `#!/usr/bin/python3`
         
          * ## Files
         
          * | File | Description |
          * | :--- | :--- |
          * | `1-safe_print_integer.py` | A function that prints an integer with `"{:d}".format()`. It uses `try` and `except` to catch errors if the value is not an integer. Returns `True` if successful, `False` otherwise. |
          * | `2-safe_print_list_integers.py` | A function that prints the first `x` elements of a list and only integers. It skips non-integer types silently and handles cases where `x` is larger than the list length. |
          * | `3-safe_print_division.py` | A function that divides two integers and prints the result. It utilizes `finally` to ensure the result (or `None`) is printed regardless of success or failure. |
          * | `4-list_division.py` | A function that divides two lists element by element. It handles `ZeroDivisionError`, `TypeError` (wrong type), and `IndexError` (out of range) and returns a new list of results. |
          * | `5-raise_exception.py` | A function that deliberately raises a `TypeError`. |
          * | `6-raise_exception_msg.py` | A function that raises a `NameError` with a provided custom message. |
