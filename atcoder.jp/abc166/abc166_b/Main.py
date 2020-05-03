n,k = map(int,input().split())
N = list(range(1,n+1))
A = set()
count = 0
for i in range(k):
  d = int(input())
  Ad = list(map(int,input().split()))
  for j in range(d):
    A.add(Ad[j])

for i in range(n):
  if N[i] in A:
    count += 1

print(n-count)