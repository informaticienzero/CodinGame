import string
from sys import stderr
from typing import List

x: str = input()
n: int = int(input())

first, number, last = x.split('-')
number: int = int(number)

# Each time we make a 999 loop, we increase a letter.
number_inc: int = n % 999
print(f'Number inc: {number_inc}', file = stderr)

# Last letter depends of the number.
last_letter_2_inc: int = n // 999
last_letter_2_index: int = string.ascii_uppercase.index(last[1])
if number_inc + number > 999:
    last_letter_2_inc += 1
last_letter_2: str = string.ascii_uppercase[(last_letter_2_index + last_letter_2_inc) % 26]
print(f'Last letter n°2 inc: {last_letter_2_inc}', file = stderr)


# First letter of last section depends on the last letter of the last section.
last_letter_1_inc: int = last_letter_2_inc // 26
last_letter_1_index: int = string.ascii_uppercase.index(last[0])
if last_letter_2_index + (last_letter_2_inc % 26) > 26:
    last_letter_1_inc += 1
last_letter_1: str = string.ascii_uppercase[(last_letter_1_index + last_letter_1_inc) % 26]
print(f'Last letter n°1 inc: {last_letter_1_inc}', file = stderr)


# Last letter of the first section depends on the first letter of the last section.
first_letter_2_inc: int = last_letter_1_inc // 26
first_letter_2_index: int = string.ascii_uppercase.index(first[1])
if last_letter_1_index + (last_letter_1_inc % 26) > 26:
    first_letter_2_inc += 1
first_letter_2: str = string.ascii_uppercase[(first_letter_2_index + first_letter_2_inc) % 26]
print(f'First letter n°2 inc: {first_letter_2_inc}', file = stderr)


# First letter of the first section depends on the last letter of the first section.
first_letter_1_inc: int = first_letter_2_inc // 26
first_letter_1_index: int = string.ascii_uppercase.index(first[0])
if first_letter_2_index + (first_letter_2_inc % 26) > 26:
    first_letter_1_inc += 1
first_letter_1: str = string.ascii_uppercase[(first_letter_1_index + first_letter_1_inc) % 26]
print(f'First letter n°1 inc: {first_letter_1_inc}', file = stderr)


number = (number + number_inc) % 999
print(first_letter_1 + first_letter_2 + '-' + str(number).zfill(3) + '-' + last_letter_1 + last_letter_2)
