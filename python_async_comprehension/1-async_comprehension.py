#!/usr/bin/env python3
"""
Async comprehension over an async generator
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension
    over async_generator and returns them as a list.
    """
    return [number async for number in async_generator()]
