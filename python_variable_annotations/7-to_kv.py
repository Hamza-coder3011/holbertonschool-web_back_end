#!/usr/bin/env python3
"""
This module provides a function to create a key-value tuple
where the value is squared.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is k and
    the second is v squared."""
    return (k, float(v * v))
