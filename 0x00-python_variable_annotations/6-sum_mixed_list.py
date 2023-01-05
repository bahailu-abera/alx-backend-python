#!/usr/bin/env python3
"""
Module sum mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Returns the sum of mxd_list as a float
    """
    return float(sum(mxd_lst))
