import math
import sys

def moore(p, x):
    return 1 - (math.log(2) * p * 2 ** (1 - 2 * x / 3)) / 3

p = float(input())
left = 0
right = 10 ** 18
while left <= right:
    half = (left + right) / 2
    #print(half)
    if moore(p, half) < 0:
        left = half
    elif moore(p, half) > 0:
        right = half
    if abs(moore(p, half)) < 10 ** -8:
        ans = moore(p, half)
        break
    if half == 0.0:
        print(p)
        sys.exit()
    #print(half, left, right, sym.diff(y, x).subs(x, half))
print(p / (2 ** (2 * half / 3)) + half)
#print(moore(p, half), half)
