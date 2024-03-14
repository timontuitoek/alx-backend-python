#!/usr/bin/env python3
"""def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the integers and floats in the mixed list.
    """
    return sum(mxd_lst)
