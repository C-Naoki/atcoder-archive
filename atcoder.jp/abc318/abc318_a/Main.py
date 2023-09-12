import math


n, m, p = map(int, input().split())

if n - m < 0:
  print(0)
else:
  print(math.ceil((n - m + 0.01) / p))
