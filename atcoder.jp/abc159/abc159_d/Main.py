import collections
n = int(input())
A = list(map(int,input().split()))
B = collections.Counter(A)
C = B.copy()
total = 0
for i in B.values():
    total += i*(i-1)//2
for i in A:
    print(total - B[i]+1)