#!/usr/bin/env python3

'''The module is a coroutine called async_generator that takes no arguments.
    It loops 10 times and each time asynchronously waits 1
    second, then yields a random number between 0 and 10. It Uses the
    random module.
'''

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """generates random values asynchronously """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)















