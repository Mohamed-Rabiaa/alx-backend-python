#!/usr/bin/env python3
"""
This module contains the task_wait_random function
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for the 'wait_random' coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for the 'wait_random'
        coroutine.

    Returns:
        asyncio.Task: The asyncio Task object for the 'wait_random' coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
