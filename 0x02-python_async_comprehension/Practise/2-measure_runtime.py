#!/usr/bin/env python3

""" Async Comprehensions in parallel """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes the async_comprehension coroutine four times in parallel and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    total_runtime = end - start
    return (total_runtime)
