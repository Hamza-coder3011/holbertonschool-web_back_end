#!/usr/bin/env python3
"""
This module defines a function that creates an asyncio.Task for the
wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random with max_delay.

    Args:
        max_delay (int): Maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: A Task object running the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
