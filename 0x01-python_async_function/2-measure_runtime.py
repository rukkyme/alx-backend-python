#!/usr/bin/env python3
"""Defines a function that measures execution time"""
import asyncio
from typing import List
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the average time taken for coroutines to complete"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n