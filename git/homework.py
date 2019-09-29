"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def base_types_exceptions_loops():
    pass


def is_two_object_has_same_value(a, b) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    if a == b:
        c = True
    else:
        c = False
    return c
    pass


def is_two_objects_has_same_type(a, b) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if type(a) == type(b):
        c = True
    else:
        c = False
    return c
    pass


def is_two_objects_is_the_same_objects(a, b) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if a is b:
        c = True
    else:
        c = False
    return c
    pass


def multiple_ints(a, b) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    d = 2
    d = type(d)
    if type(a) == d and type(b) == d:
        c = a * b
    else:
        raise ValueError('At least one element is not integer')
    return c
    pass


def multiple_ints_with_conversion(a, b) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.



    Examples:
        multiple_ints_with_conversion(6, 6)

        multiple_ints_with_conversion(2, 2.0)

        multiple_ints_with_conversion("12", 1)

        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")

    """
    d = 2
    if type(int(a)) == type(d) and type(int(b)) == type(d):
        c = int(a) * int(b)
    else:
        raise ValueError('Not valid input data')
    return c
    pass



def is_word_in_text(what_word, where_word) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
       '' >>> True
        is_word_in_text("Glad", "Nice to meet you ")
       '' >>> False

    """
    if where_word.find(what_word) != -1:
        c = True
    else:
        c = False
    return c


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    i = 0
    results=[]
    while i<13:
        results.append(i)
        i=i+1
    del results[6]
    del results[6]
    return results


def remove_from_list_all_negative_numbers(in_list) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
       '''''' >>> [1, 5, 8]
    """
    i = 0
    while i < len(in_list):
        if in_list[i] < 0:
            del in_list[i]
        else:
            i = i + 1
    return in_list


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}

    """
    dicts = {}
    i = 1
    while i < 27:
        dicts[i] = chr(96 + i)
        i = i + 1
    return dicts


def simple_sort(ls_1) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
       '' >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    ls_2=[]
    while len(ls_1) > 0:
        ls_2.append(min(ls_1))
        b = ls_1.index(min(ls_1))
        del ls_1[b]
    return ls_2
    pass
