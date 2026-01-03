#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Args:
        my_list_1: First list.
        my_list_2: Second list.
        list_length: Number of elements to divide.

    Returns:
        A new list of length list_length with all divisions.
    """
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
