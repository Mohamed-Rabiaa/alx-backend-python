#!/usr/bin/env python3
"""
This module contains the async_comprehension function
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    This coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.

    Returns:
      a list of 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
