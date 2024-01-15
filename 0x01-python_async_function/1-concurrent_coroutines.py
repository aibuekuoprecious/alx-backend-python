#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List
from heapq import heappush

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Parameters:
    n (int): Number of times to spawn wait_random.
    max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
    List[float]: List of all the delays in ascending order.
    """
    heap = []
    for _ in range(n):
        heappush(heap, await wait_random(max_delay))
        return list(heap)
