import sys
import math

def sum_of_sums(n):
    total = n
    
    i = 2
    half = n // 2
    
    while i <= n:
        if i <= half:
            total += i * (n // i)
        else:
            total += i
        i += 1
        
    return total

n = int(input())
print(sum_of_sums(n))
