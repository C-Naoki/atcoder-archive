from itertools import permutations
n = int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

num = [0]*n
for i in range(n):
    num[i] = i+1

cnt = 1
for i in permutations(num):
    if P == list(i):
        a = cnt + 1
    if Q == list(i):
        b = cnt + 1
    cnt += 1
print(abs(a-b))