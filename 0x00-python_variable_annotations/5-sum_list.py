#!/usr/bin/env python3
'''
This module contains the sum_list function
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    This function takes a list input_list of floats as argument
    and returns their sum as a float

    Args:
      input_list: list of floats

    Returns:
      the sum of the floats in the list
    '''
    sum = 0.0
    for f in input_list:
        sum += f

    return sum
