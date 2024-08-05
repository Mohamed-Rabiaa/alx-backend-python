#!/usr/bin/env python3
"""
This module contains the measure_time function
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """
    Measure the average time taken to run the 'wait_n' function.

    Args:
        n (int): The number of times to run 'wait_random' concurrently
        in 'wait_n'.
        max_delay (int): The maximum delay in seconds for each
        'wait_random' call.

    Returns:
        float: The average time taken per task.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
