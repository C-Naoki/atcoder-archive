from itertools import combinations

A = list(map(int,input().split()))
for i in range(4):
    if A[i] == sum(A) - A[i]:
        print('Yes')
        exit()
for i, j in combinations(range(4),2):
    if A[i] + A[j] == sum(A) - (A[i] + A[j]):
        print('Yes')
        exit()

print('No')