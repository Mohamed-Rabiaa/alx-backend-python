#!/usr/bin/env python3
"""
This module contains the wait_n function
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Run 'wait_random' function 'n' times concurrently and return the list
    of delays in the order they complete.

    Args:
        n (int): The number of times to run 'wait_random' concurrently.
        max_delay (int): The maximum value for the random delay in seconds
        for each 'wait_random' call.

    Returns:
        List[float]: A list of delay times in the order they completed.
    """
    results = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(results)
