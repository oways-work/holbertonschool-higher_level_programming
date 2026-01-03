#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
        my_list: The list to print from.
        x: The number of elements to access.

    Returns:
        The real number of integers printed.
    """
    nb_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_printed += 1
        except (ValueError, TypeError):
            pass
    print("")
    return nb_printed
