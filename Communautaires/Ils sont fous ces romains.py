import sys
import math
import collections

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

table = collections.OrderedDict()
table['M'] = 1000
table['CM'] = 900
table['D'] = 500
table['CD'] = 400
table['C'] = 100
table['XC'] = 90
table['L'] = 50
table['XL'] = 40
table['X'] = 10
table['IX'] = 9
table['V'] = 5
table['IV'] = 4
table['I'] = 1


def rom_to_classic(roman):
    total = 0
    for key in table:
        while roman.startswith(key):
            total += table[key]
            roman = roman[len(key) : ]
    return total
    
    
def classic_to_roman(integer):
    result = []
    for key in table:
        while table[key] <= integer:
            integer -= table[key]
            result.append(key)
    return ''.join(result)
    

rom_1 = input()
int_1 = rom_to_classic(rom_1)

rom_2 = input()
int_2 = rom_to_classic(rom_2)

print(classic_to_roman(int_1 + int_2))