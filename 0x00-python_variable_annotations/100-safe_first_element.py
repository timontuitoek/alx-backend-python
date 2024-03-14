#!/usr/bin/env python3
"""def safe_first_element(lst: List[Any]) -> Union[Any, None]"""
from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list safely.
    """
    if lst:
        return lst[0]
    else:
        return None
