#!/usr/bin/env python3
'''
This module contains the element_length function
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    This function takes an iterable and returns a list of tuples that has
    a sequence and an integer

    Args:
      lst: an iterable

    Returns:
       a list of tuples that has a sequence and an integer
    '''
    return [(i, len(i)) for i in lst]
