from sys import stderr
from typing import List

n = int(input())
input: List[str] = input().split()
numbers: List[int] = [int(x) for x in input if x.isdigit()]

result: str = ''
if '-' in input:
    result += '-'
    numbers = list(sorted(numbers))
    for number in numbers:
        result += str(number)
    
    if '.' in input:
        result = result[0:2] + '.' + result[2:]
        
else:
    numbers = list(reversed(sorted(numbers)))
    for number in numbers:
        result += str(number)
    
    # Case of a positive number.
    if '.' in input:
        # Case of a positive floating number.
        result = result[:-1]
        result += '.'
        result += str(numbers[-1])
        
        
# Because we don't want trailing zero.
result = result.rstrip('0')
# Because we don't want the last point if we got an integer.
if result[-1] == '.':
    result = result[:-1]

# Because if it's 0, it's 0, yeah !
if float(result) == 0:
    print(0)
else:
    print(result)
