# Python - More Classes and Objects

This project continues the exploration of Object-Oriented Programming (OOP) in Python. It focuses on the definition of the `Rectangle` class and gradually adds functionality such as property getters/setters, area/perimeter calculation, string representation (`__str__`, `__repr__`), instance deletion handling, static methods, and class methods.

## Files

* **0-rectangle.py**: Defines an empty class `Rectangle`.
* **1-rectangle.py**: Adds private instance attributes `width` and `height` with property getters and setters for validation.
* **2-rectangle.py**: Adds public instance methods `area()` and `perimeter()`.
* **3-rectangle.py**: Adds `__str__` method to print the rectangle using `#`.
* **4-rectangle.py**: Adds `__repr__` method to return a string representation of the rectangle for `eval()`.
* **5-rectangle.py**: Adds `__del__` method to print a message upon instance deletion.
* **6-rectangle.py**: Adds a public class attribute `number_of_instances` that tracks the count of existing instances.
* **7-rectangle.py**: Adds a public class attribute `print_symbol` to customize the character used for string representation.
* **8-rectangle.py**: Adds a static method `bigger_or_equal(rect_1, rect_2)` to compare rectangles by area.
* **9-rectangle.py**: Adds a class method `square(cls, size=0)` to create a new Rectangle instance acting as a square.
