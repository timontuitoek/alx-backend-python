#!/usr/bin/env python3
import asyncio
import random
from typing import List

async def async_generator() -> List[int]: # type: ignore
    """Generate a list of random numbers asynchronously"""
    for _ in range(10):
        yield random.randint(0, 10)

async def async_comprehension() -> List[int]:
    """Generate a list of random numbers asynchronously"""
    return [random.randint(0, 10) for _ in range(10)]

async def measure_runtime() -> float:
    """Iterate over the values yielded by async_generator"""
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    # End time measurement
    end_time = asyncio.get_event_loop().time()

    # Calculate total runtime
    total_runtime = end_time - start_time

    return total_runtime


async def main() -> None:
    # Print the total runtime returned by measure_runtime
    print(await measure_runtime())


if __name__ == "__main__":
    asyncio.run(main())
