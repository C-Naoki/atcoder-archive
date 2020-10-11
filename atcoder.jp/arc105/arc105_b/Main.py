from math import gcd

n = int(input())
A = list(map(int,input().split()))

chk = A[0]
for i in range(1,n):
    chk = gcd(chk,A[i])

print(chk)