import sys
import math

# Thanks StackOverflow <3
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

expression = input()
to_print = "true";

if expression.count('(') == expression.count(')') and expression.count('[') == expression.count(']') and expression.count('{') == expression.count('}'):
    # If the count if good, let's check we have a closing one in a position greater than a openning one.
    chars = ['(', ')', '[', ']', '{', '}']
    
    char_index = 0;
    while char_index < len(chars):
        openning = find(expression, chars[char_index])
        closing = find(expression, chars[char_index + 1])
        
        index = 0
        while index < len(openning):
            if (openning[index] > closing[index]):
                to_print = "false"
                break
            index = index + 1
        
        char_index = char_index + 2
else:
    to_print = "false"

print(to_print)
