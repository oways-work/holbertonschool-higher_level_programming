# Python - Input/Output

This project covers file handling in Python, including reading, writing, and appending to files, as well as JSON serialization and deserialization.

## Function Prototypes

| File | Prototype |
| --- | --- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |

## Tasks

* **0. Read file**
    * `0-read_file.py`: Function that reads a text file (UTF8) and prints it to stdout.

* **1. Write to a file**
    * `1-write_file.py`: Function that writes a string to a text file (UTF8) and returns the number of characters written.

* **2. Append to a file**
    * `2-append_write.py`: Function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

* **3. To JSON string**
    * `3-to_json_string.py`: Function that returns the JSON representation of an object (string).

* **4. From JSON string to Object**
    * `4-from_json_string.py`: Function that returns an object (Python data structure) represented by a JSON string.

* **5. Save Object to a file**
    * `5-save_to_json_file.py`: Function that writes an Object to a text file using a JSON representation.

* **6. Create object from a JSON file**
    * `6-load_from_json_file.py`: Function that creates an Object from a “JSON file”.

* **7. Load, add, save**
    * `7-add_item.py`: Script that adds all arguments to a Python list and then saves them to a file.

* **8. Class to JSON**
    * `8-class_to_json.py`: Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

* **9. Student to JSON**
    * `9-student.py`: Class `Student` that defines a student by public instance attributes `first_name`, `last_name`, and `age`, and a method `to_json()` that retrieves a dictionary representation of a `Student` instance.

* **10. Student to JSON with filter**
    * `10-student.py`: Updates `9-student.py` with a `to_json(self, attrs=None)` method that retrieves a dictionary representation of a `Student` instance with an optional list of attributes to filter.

* **11. Student to disk and reload**
    * `11-student.py`: Updates `10-student.py` with a `reload_from_json(self, json)` method that replaces all attributes of the `Student` instance.

* **12. Pascal's Triangle**
    * `12-pascal_triangle.py`: Function that returns a list of lists of integers representing the Pascal’s triangle of `n`.
