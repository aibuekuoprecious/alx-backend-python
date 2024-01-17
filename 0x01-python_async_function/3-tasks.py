#!/usr/bin/env python3
""" Async basics """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
     Function that takes an integer max_delay and returns an asyncio.Task.

     This function creates an asyncio.Task that wraps the wait_random coroutine.
     The Task object represents a computation being done and can be awaited to get
     its eventual result.

     Parameters:
     max_delay (int): Maximum delay in seconds for wait_random.

     Returns:
     asyncio.Task: Task object that represents a computation being done.
     """
    task = create_task(wait_random(max_delay))
    return task
