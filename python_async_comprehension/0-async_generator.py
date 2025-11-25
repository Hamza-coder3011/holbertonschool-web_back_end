#!/usr/bin/env python3
"""
This module provides a method
"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random floats between 0 and 10,
    waiting 1 second between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
