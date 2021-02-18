import sys

from itertools import combinations

n = input()
n = list(n)
k = len(n)
for i in range(k,0,-1):
    for l in combinations(n, i):
        #print(l)
        S = 0
        for j in l:
            #print(j)
            num = int(j)
            S += num
        if S % 3 == 0:
            print(k - i)
            sys.exit()
print(-1)