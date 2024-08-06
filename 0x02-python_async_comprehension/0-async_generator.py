#!/usr/bin/env python3
"""
This module contains the async_generator function
"""

import asyncio
import random
import typing


async def async_generator() -> typing.AsyncIterator[float]:
    """
    This coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10 Using the random module.

    Return:
      an asynchronous generator object that yield random floats.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
