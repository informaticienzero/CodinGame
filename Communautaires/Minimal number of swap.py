from sys import stderr
from typing import List


def all_one_aligned(digits: List[int]) -> bool:
    """
    Checks if all the 1 are aligned from the beginning of the list.
    """
    to_check: List[int] = digits[0:digits.count(1)]
    return all(x == 1 for x in to_check)


digits: List[int] = []
total: int = 0

n: int = int(input())
for i in input().split():
    digits.append(int(i))

if 0 not in digits:
    print(0)
else:
    index: int = 0
    
    while not all_one_aligned(digits):
        if digits[index] == 0:
            # We'll replace the last 1 we find by a 0.
            last_occurence: int = -1
            for i in range(-1, -(len(digits) + 1), -1):
                if digits[i] == 1:
                    last_occurence = i
                    break
            
            total += 1
            digits[index] = 1
            digits[last_occurence] = 0
            
        index += 1
            
    print(total)
