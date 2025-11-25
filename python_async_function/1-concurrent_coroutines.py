#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that spawns multiple wait_random
coroutines concurrently and returns their results
in ascending order of completion.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay and return a list of all delays
    in ascending order of completion.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay to pass to wait_random.

    Returns:
        List[float]: List of delays in ascending order without using sort().
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []

    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)

    return results
