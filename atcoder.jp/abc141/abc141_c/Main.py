n, k, q = map(int,input().split())
P = [0]*n
Q = [k]*n
for i in range(q):
    a = int(input())
    P[a - 1] += 1
for i in range(n):
    Q[i] -= (q - P[i])
for i in range(n):
    if Q[i] > 0:
        print('Yes')
    else:
        print('No')