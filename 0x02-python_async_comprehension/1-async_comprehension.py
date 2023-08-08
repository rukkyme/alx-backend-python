#!/usr/bin/env python3


'''The coroutine collects 10 random numbers using an async comprehension
    over async_generator, then return the 10 random numbers.
'''

from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """asynchronously comprehensing over async_generator"""
    return [i async for i in async_generator()]








