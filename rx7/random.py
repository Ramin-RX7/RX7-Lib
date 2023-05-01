'''
random Variable Generator Class.
(ALL FUNCTIONS ARE STATIC METHODS)
'''

import random as _random
from typing import Iterable



def choose(iterable:Iterable, k:int=1, duplicate=True):
    """
    Return a random element from a non-empty sequence.
    Args:
        iterator (Iterator): The iterator you wanna choose a random member of it
        k (int): number of items to randomly get from iterator
        duplicate (bool): wether or not getting duplicate items (if k>1)
    Returns:
        Any: one of members of iterator if k=1
        List[Any]: if k>1
    Raise:
        ValueError: Occurs when k<1
    """
    if type(k) != int:
        raise TypeError('k must be integer.')
    if k == 1:
        return _random.choice(iterable)
    elif k > 1:
        if duplicate:
            return _random.choices(iterable,k=k)
        else:
            return _random.sample(iterable,k=k)
    else:
        raise ValueError('k Must Be Higher 0')


def integer(first_number:int, last_number:int):
    """
    Return random integer in range [a, b], including both end points.
    Args:
        first_number (int):  a
        last_number  (int):  b
    Return:
        int: a random number in [a, b] range
    """
    return _random.randint(first_number,last_number)


def O1(decimal_number:int = 17):
    """
    Return x in the interval [0, 1)
    Arg:
        decimal_number (int): how many decimal numbers to round
    Return:
        float: random number in interval [0,1)
    """
    return round(_random.random(),decimal_number)


def number(first_number:float, last_number:float):
    """
    Return x in the interval [a, b]
    Args:
        first_number (float):  a
        last_number  (float):  b
    Return:
        flaot: a random number in interval [a, b]
    """
    return _random.uniform(first_number,last_number)


def shuffle(iterable:Iterable):
    """
    Return shuffled version of iterable
    Arg:
        iterable (Iterable): The iterable you want to shuffle it's items
    Return:
        Iterable[Any]: shuffled version of given iterable
    """
    # copied = type(iterable)(iterable)
    # random.shuffle(copied)
    # return copied
    real_type = type(iterable)
    new_iterable = list(iterable)
    _random.shuffle(new_iterable)
    if real_type in (set,tuple):
        return real_type(new_iterable)
    elif real_type == str:
        return ''.join(new_iterable)
    elif real_type == dict:
        return {item:iterable[item] for item in new_iterable}
    else:
        return new_iterable
