n = int(input())
A = list(map(int,input().split()))

b = 1
B=[0]*(n+1)
count = 0

t=len(A)-1
for i in range(t):
    B[i] = b
    if 2*(b - A[i]) < A[i+1]:
        count += 1
        break
    b = 2*(b - A[i])
B[n] = b

if n == 0 and A[0] > 1:
    count += 1

j = 0
while count == 0 and A[t] > B[j]:
    if j == n:
        break
    j += 1

total = 0
for i in range(j):
    total += B[i]

s = A[t]
for i in range(t-1,j-1,-1):
    total += min(B[i],s+A[i])
    s+=A[i]

if count==0:
    print(total+A[t])
else:
    print('-1')