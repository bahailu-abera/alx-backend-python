#!/usr/bin/env python3
"""
Module concurrent coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of all delays
    """
    delays: List[float] = []

    while n > 0:
        delay = await wait_random(max_delay)
        delays.append(delay)
        n -= 1
    return delays
