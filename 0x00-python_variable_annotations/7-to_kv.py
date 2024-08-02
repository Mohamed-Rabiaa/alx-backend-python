#!/usr/bin/env python3
'''
This module contains the to_kv function
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    This function  takes a string k and an int OR float v
    as arguments and returns a tuple

    Args:
      k: a string
      v: an integer or a float

    Returns:
      a tuple where The first element is the string k.
      The second element is the square of the int/float v
    '''
    return (k, v * v)
