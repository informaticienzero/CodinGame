from sys import stderr
from time import process_time
from typing import Dict, List


def calculate_possibilities(max: int) -> Dict[int, int]:
    """Calculate the numbers of lucky numbers from 0 to 10**(max - 1)"""
    possibilities: Dict[int, int] = { 0: 0, 1: 2 }
    index: int = 2
    while index < max:
        possibilities[index] = 2 * (9 ** (index - 1)) + 8 * possibilities[index - 1]
        index += 1
    return possibilities


def get_digits(number: int) -> List[int]:
    """
    Gets the list of all digits of a number, from left to right.
    """
    digits: List[int] = []

    if number < 10:
        return [number]
    return [int(c) for c in str(number)]


def count(number: int) -> int:
    """
    Count the lucky numbers from 0 to number with a fast mathematic range.
    """
    digits: List[int] = get_digits(number)
    pow_10: int = len(digits) - 1
    possibilities: Dict[int, int] = calculate_possibilities(pow_10 + 1)
    lucky_numbers: int = 0

    found_lucky_digit: bool = False
    lucky_digit: int = -1

    for digit in digits:
        if not found_lucky_digit:
            # We're in the classic case.
            if digit == 7:
                lucky_numbers += 6 * possibilities[pow_10] + 9 ** pow_10
            elif digit == 8:
                lucky_numbers += 7 * possibilities[pow_10] + 9 ** pow_10
            elif digit == 9:
                lucky_numbers += 7 * possibilities[pow_10] + 2 * (9 ** pow_10)
            else:
                lucky_numbers += digit * possibilities[pow_10]
        else:
            # Things change now that we know we have a lucky digit before us.
            if digit == 6:
                lucky_numbers += 6 * (9 ** pow_10)
                if found_lucky_digit and lucky_digit != 6:
                    # We'll find no more lucky numbers.
                    return lucky_numbers

            elif digit == 7:
                if lucky_digit == 6:
                    lucky_numbers += 7 * (9 ** pow_10)
                else:
                    lucky_numbers += 6 * (9 ** pow_10)

            elif digit == 8:
                lucky_numbers += 7 * (9 ** pow_10)
                if found_lucky_digit and lucky_digit != 8:
                    # We'll find no more lucky numbers.
                    lucky_numbers += 9 ** pow_10
                    return lucky_numbers

            elif digit == 9:
                lucky_numbers += 8 * (9 ** pow_10)
            else:
                lucky_numbers += digit * (9 ** pow_10)

        pow_10 -= 1

        if not found_lucky_digit and (digit == 6 or digit == 8):
            lucky_digit = digit
            found_lucky_digit = True

    return lucky_numbers
    

l, r = [int(i) for i in input().split()]
start: float = process_time()

if l == r:
    # We know that if they are the same, no need to make calculus.
    if ('6' in str(l)) ^ ('8' in str(l)):
        print(1)
    else:
        print(0)
else:
    until_l: int = count(l)
    until_r: int = count(r + 1)
    print(until_r - until_l)

end: float = process_time()
print(f'Solution found in {(end - start):03.03f}s.', file = stderr)
