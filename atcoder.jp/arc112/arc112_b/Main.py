b, c = map(int, input().split())
plus_left = b - c // 2
plus_right = b + max(0, (c-2) // 2)
minus_left = -b - (c-1) // 2
minus_right = -b + (c-1) // 2
m = min(plus_left, minus_left)
M = max(plus_right, minus_right)
if plus_left <= minus_right:
    print(M - m + 1)
else:
    print(plus_right - plus_left + minus_right - minus_left + 2)