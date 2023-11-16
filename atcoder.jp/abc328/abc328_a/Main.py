import numpy as np


n, x = map(int, input().split())
S = np.array(list(map(int, input().split())))
print(S[S <= x].sum())
