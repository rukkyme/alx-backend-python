#!/usr/bin/env python3

import asyncio
from random import uniform

''' Asynchronous coroutine that waits for a random delay between 0 and max_delay 
    seconds.
    Args:max_delay (float, optional): The maximum delay in seconds. Defaults to 10.
    Returns:float: The random delay that was waited for.
'''
async def wait_random(max_delay: int = 10) -> float:
    
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))