import numpy as np

n = int(input())
A = np.array(list(map(int, input().split()))).reshape(-1, 7).sum(axis=1)
for a in A:
  print(a, end=" ")