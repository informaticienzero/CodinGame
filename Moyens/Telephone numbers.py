import sys

numbers = []
n = int(input())
for i in range(n):
    telephone = input()
    numbers.append(telephone)
    
sorted(numbers)

# Here the fun begins.
tree = dict()
total = 0

for number in numbers:

    previous = tree

    for digit in number:
        keys = previous.keys()
        if digit in keys:
            #print('There is already {} in {}'.format(digit, keys), file = sys.stderr)
            pass
        else:
            previous[digit] = {}
            total += 1

        previous = previous[digit]
            
print(total)
