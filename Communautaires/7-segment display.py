from enum import Enum
from sys import stderr
from typing import List


class Side(Enum):
    """
    Where should be printed the character?
    """
    Left: int = 1
    Right: int = 2
    Both: int = 3


def get_vertical(character: str, spaces: int, side: Side) -> str:
    """
    Prints twice the given character with as much spaces between them as required.
    """
    if side == Side.Left:
        return character + ' ' * (spaces + 1)
    elif side == Side.Right:
        return ' ' * (spaces + 1) + character
    else:
        return character + ' ' * spaces + character
        

def get_horizontal(character: str, count: int) -> str:
    """
    Prints an horizontal line of the given character, count times.
    """
    return ' ' + character * count + ' '


def generate(number: int, character: str, spaces: int) -> List[str]:

    generation: List[str] = []
    
    # Complete configuration, goes for 8.
    upper_horizontal = get_horizontal(c, spaces)
    upper_sides = get_vertical(c, spaces, Side.Both)
    middle = upper_horizontal
    lower_sides = upper_sides
    lower_horizontal = upper_horizontal

    if number == 1:
        upper_horizontal = get_horizontal(' ', spaces)
        upper_sides = get_vertical(c, spaces, Side.Right)
        middle = upper_horizontal
        lower_sides = get_vertical(c, spaces, Side.Right)
        lower_horizontal = upper_horizontal

    elif number == 2:
        upper_sides = get_vertical(c, spaces, Side.Right)
        lower_sides = get_vertical(c, spaces, Side.Left)

    elif number == 3:
        upper_sides = get_vertical(c, spaces, Side.Right)
        lower_sides = get_vertical(c, spaces, Side.Right)

    elif number == 4:
        upper_horizontal = get_horizontal(' ', spaces)
        lower_sides = get_vertical(c, spaces, Side.Right)
        lower_horizontal = upper_horizontal

    elif number == 5:
        upper_sides = get_vertical(c, spaces, Side.Left)
        lower_sides = get_vertical(c, spaces, Side.Right)

    elif number == 6:
        upper_sides = get_vertical(c, spaces, Side.Left)

    elif number == 7:
        upper_sides = get_vertical(c, spaces, Side.Right)
        middle = get_horizontal(' ', spaces)
        lower_sides = get_vertical(c, spaces, Side.Right)
        lower_horizontal = middle

    elif number == 9:
        lower_sides = get_vertical(c, spaces, Side.Right)
        
    elif number == 0:
        middle = get_horizontal(' ', spaces)

    generation.append(upper_horizontal)
    for i in range(0, spaces):
        generation.append(upper_sides)
    generation.append(middle)
    for i in range(0, spaces):
        generation.append(lower_sides)
    generation.append(lower_horizontal)

    return generation


n: str = input()
c: str = input()
s: int = int(input())

numbers: List[List[str]] = []
digits: List[int] = [int(c) for c in n]
for digit in digits:
    numbers.append(generate(digit, c, s))

result: List[str] = []
for i in range(2 * s + 3):
    s: str = ''
    for number in numbers:
        s += number[i] + ' '
    result.append(s.rstrip())
    
print(*result, sep = '\n')
