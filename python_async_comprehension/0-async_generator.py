#!/usr/bin/env python3
"""
Async generator that yields 10 random numbers asynchronously
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates 10 random floats between 0 and 10,
    waiting 1 second between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
