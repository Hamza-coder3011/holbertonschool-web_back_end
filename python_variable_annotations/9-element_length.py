#!/usr/bin/env python3
"""
This module provides a function to generate a list of tuples containing
elements of an iterable and their lengths.
"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]
