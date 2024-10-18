from typing import Generator, Callable
import re

G = Generator[float, None, None]


def generator_numbers(string: str) -> G:
    pattern = r"-?\d+\.?\d*"
    numbers = re.findall(pattern, string)
    print(numbers)
    for num in numbers:
        yield float(num)


def sum_profit(string: str, func: Callable) -> float:
    generator = func(string)
    return sum([x for x in generator])
