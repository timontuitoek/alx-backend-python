#!/usr/bin/env python3
"""
provides coroutines for generating random delays
and waiting for multiple delays.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """
    Asynchronously spawns wait_random n times with the specified max_delay.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
