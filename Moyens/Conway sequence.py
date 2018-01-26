from itertools import groupby
from sys import stderr
from typing import List


def conway(start: int, max: int) -> List[str]:
    """
    Calculates the Conway sequence until a max, starting from a given number.

    Args:
        start (int) - The starting value of the sequence.
        max (int) - The maximum lines to calculate.
    """
    line: str = str(start)
    result: List[str] = [line]

    for i in range(max + 1):
        numbers: List[int] = [int(x) for x in line.split()]

        # Function groupby returns consecutive keys and groups from an iterable object.
        # [key for key, group in groupby([1, 1, 2, 3, 1, 25])] --> [1, 2, 3, 1, 25]
        # [list(group) for key, group in groupby([1, 1, 2, 3, 1, 25])] --> [[1, 1], [2], [3], [1], [25]]
        line = ' '.join(str(len(list(group))) + ' ' + str(key) for key, group in groupby(numbers))
        result.append(line)

    return result


r = int(input())
l = int(input())

conway: List[str] = conway(r, l)
# -1 because first line is index 1 and not 0.
print(conway[l - 1])
