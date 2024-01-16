#!/usr/bin/env python3

""" Async Generator """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ 
    Asynchronously generates a sequence of 10 random float numbers in the range [0, 10].
    Each number is generated after a delay of 1 second.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
