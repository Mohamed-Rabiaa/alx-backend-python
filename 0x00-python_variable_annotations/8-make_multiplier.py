#!/usr/bin/env python3
'''
This module contains the make_multiplier function
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    This function takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier

    Args:
      multiplier: a float

    Returns:
      a function that multiplies a float by multiplier
    '''
    def fun(n: float):
        return n * n

    return fun
