#!/usr/bin/env python3
"""
This module defines a coroutine that spawns multiple asyncio.Tasks of
wait_random concurrently and returns their results in
ascending order of completion.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn task_wait_random n times with max_delay and return a list
    of all delays in ascending order of completion.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay to pass to each task.

    Returns:
        list[float]: List of delays in ascending order without using sort().
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
