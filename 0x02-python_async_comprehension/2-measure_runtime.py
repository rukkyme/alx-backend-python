#!/usr/bin/env python3


''' Measure_runtime coroutine should measure the total runtime 
and return it.
'''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time









