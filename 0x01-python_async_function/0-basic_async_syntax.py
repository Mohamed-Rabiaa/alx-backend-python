#!/usr/bin/env python3
'''
This module contains the wait_random function
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    This function takes in an integer argument (max_delay,
    with a default value of 10) and waits for a random delay
    between 0 and max_delay (included and float value)
    seconds and eventually returns it

    Args:
      max_delay (int): the max delay that the function can wait before
      finish executing

    Return:
      the random floating number between 0 and max_delay
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
