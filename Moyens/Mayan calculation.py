from re import findall
from sys import stderr
from typing import Dict, List


maya_numbers: Dict[int, str] = dict()
for i in range(0, 20):
    maya_numbers[i] = ''


def get_num_from_maya(maya_number: str) -> int:
    
    numbers: List[str] = maya_number.split('\n')
    roman_numbers: List[int] = []
    
    for number in numbers:
        for key, value in maya_numbers.items():
            if number == value:
                roman_numbers.append(key)
    
    result: int = 0
    index: int = 0
    for roman in reversed(roman_numbers):
        result += roman * (20 ** index)
        index += 1
    
    return result
    
    
def to_maya(roman_number: int, h: int) -> str:
    
    # Special case for 0. Work for even-sized str.
    if roman_number == 0:
        maya_zero: str = maya_numbers[0]
        zero_size: int = len(maya_zero)
        # https://stackoverflow.com/a/3258612/6060256
        return '\n'.join(maya_zero[i:i + 4] for i in range(0, zero_size, 4))
    
    remainders: List[int] = []
    while roman_number > 0:
        remainders.append(roman_number % 20)
        roman_number = roman_number // 20
        
    result: str = ''
    for digit in reversed(remainders):
        maya_number: str = maya_numbers[digit]
        index: int = 0
        
        for c in maya_number:
            
            result += c
            index += 1
            
            if index == h:
                index = 0
                result += '\n'
    
    return result


l, h = [int(i) for i in input().split()]
for i in range(h):
    numeral = input()
    # https://stackoverflow.com/a/9477447/6060256
    splitted_str: str = findall('.' * l, numeral)
    index: int = 0
    
    for key, value in maya_numbers.items():
        maya_numbers[key] += f'{splitted_str[index]}'
        index += 1
    
    
first_num: str = ''
counter_1: int = 0
s1 = int(input())
for i in range(s1):
    
    # Each time we reach h, it's a new number.
    if counter_1 == h:
        first_num += '\n'
        counter_1 = 0
    counter_1 += 1
    
    first_num += input()
    

second_num: str = ''
counter_2: int = 0
s2 = int(input())
for i in range(s2):
    
    if counter_2 == h:
        second_num += '\n'
        counter_2 = 0
    counter_2 += 1
    
    second_num += input()
    
operation = input()

roman_1: int = get_num_from_maya(first_num)
roman_2: int = get_num_from_maya(second_num)
roman_result: int = 0

if operation == '+':
    roman_result = roman_1 + roman_2
elif operation == '-':
    roman_result = roman_1 - roman_2
elif operation == '*':
    roman_result = roman_1 * roman_2
else:
    roman_result = roman_1 / roman_2

print(f'Roman 1: {roman_1}', file = stderr)
print(f'Roman 2: {roman_2}', file = stderr)
print(f'Roman total: {roman_result}', file = stderr)
print(to_maya(roman_result, h))
