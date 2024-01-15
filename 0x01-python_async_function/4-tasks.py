#!/usr/bin/env python3
""" The basics of async """

from typing import List
from heapq import heappush

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay.

    Parameters:
    n (int): Number of times to spawn task_wait_random.
    max_delay (int): Maximum delay in seconds for task_wait_random.

    Returns:
    List[float]: List of all the delays in ascending order.
    """
    heap = []
    for _ in range(n):
        heappush(heap, await task_wait_random(max_delay))
    return list(heap)