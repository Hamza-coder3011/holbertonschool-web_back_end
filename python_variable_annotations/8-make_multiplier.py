#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function for floats.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
