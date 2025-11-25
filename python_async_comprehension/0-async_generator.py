#!/usr/bin/env python3
"""Async generator that yields a random number every second, 10 times."""

import asyncio
import random

async def async_generator():
    """Asynchronously generate 10 random numbers between 0 and 10."""
    random.seed(42)
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
