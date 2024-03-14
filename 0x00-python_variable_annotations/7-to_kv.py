#!/usr/bin/env python3
"""def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple
    """
    return k, v ** 2.0
