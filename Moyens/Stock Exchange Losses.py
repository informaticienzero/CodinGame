from sys import stderr
from typing import List


def biggest_decrease(values: List[int]) -> int:
    """
    Gets the biggest decrease in a list of integers. If there is no, returns 0.
    # https://stackoverflow.com/a/32161433/6060256

    Args:
        values (list[int]) - List of integers.
    """
    max_value: int = values[0]
    max_drop: int = -1

    for value in values:
        if max_value < value:
            max_value = value
        else:
            drop: int = max_value - value
            max_drop = max(max_drop, drop)

    return max_drop if max_drop != -1 else 0
    

values: List[int] = []
n = int(input())
for i in input().split():
    values.append(int(i))

print(-biggest_decrease(values))
