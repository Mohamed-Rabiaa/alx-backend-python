#!/usr/bin/env python3
"""
This module contains the task_wait_n function
"""

import asyncio
import typing


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Create and run 'n' asyncio Tasks for the 'wait_random' coroutine
    concurrently, and return a sorted list of the results.

    Args:
        n (int): The number of tasks to create and run concurrently.
        max_delay (int): The maximum delay in seconds for each 'wait_random'
        coroutine.

    Returns:
        typing.List[float]: A sorted list of delays (in seconds) from all
        completed tasks.
    """
    results = await asyncio.gather(*(task_wait_random(max_delay)
                                     for _ in range(n)))
    return sorted(results)
