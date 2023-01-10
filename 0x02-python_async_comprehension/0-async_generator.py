#!/usr/bin/env python3
"""
Module async generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Returns a generator of radom numbers
    """
    for _ in range(10):
        yield random.uniform(1, 10)
        await asyncio.sleep(1)
