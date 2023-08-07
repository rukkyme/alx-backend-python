#!/usr/bin/env python3
"""Create task wait random using regular syntax"""
from asyncio import create_task, Task
wait_random = __import__("0-basic_async_syntax").wait_random

"""Creating  a new task"""
def task_wait_random(max_delay: int) -> Task:
    
    return create_task(wait_random(max_delay))