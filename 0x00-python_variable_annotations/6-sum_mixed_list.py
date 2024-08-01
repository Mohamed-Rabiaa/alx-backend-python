#!/usr/bin/env python3
'''
This module contains the sum_mixed_list function
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    This function takes a list mxd_lst of integers and floats
    and returns their sum as a float.

    Args:
      mxd_list: list of floats

    Returns:
      the sum of the floats in the list as a float
    '''
    sum = 0.0
    for n in mxd_lst:
        sum += n

    return sum
