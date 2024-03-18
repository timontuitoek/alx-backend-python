#!/usr/bin/env python3
"""
provides a function to measure the average execution time of wait_n.
"""
import asyncio
from cgitb import lookup
import time
from typing import Callable
# Importing wait_n from the previous file
from my_module import wait_n
import sys
sys.path.insert(0, './' + '../')  # Add path to #!/usr/bin/env python3

"""
This module provides a function to measure the average execution time of wait_n.
"""

import asyncio
import time
from typing import Callable

# Importing wait_n from the previous file
from my_module import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    await asyncio.gather(*[wait_n(max_delay) for _ in range(n)])
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./2-measure_runtime.py <n> <max_delay>")
        sys.exit(1)

    n = int(sys.argv[1])
    max_delay = int(sys.argv[2])

    average_time = asyncio.run(measure_time(n, max_delay))
    print(f"Average execution time per call: {average_time} seconds")


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 3
    average_time = measure_time(n, max_delay)
    print(f"Average execution time per call: {average_time} seconds")
