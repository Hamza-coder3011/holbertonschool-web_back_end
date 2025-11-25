#!/usr/bin/env python3
"""
This module measures the average runtime of the wait_n coroutine.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay) and return
    the average time per coroutine.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay to pass to each coroutine.

    Returns:
        float: Average execution time per coroutine in seconds.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
