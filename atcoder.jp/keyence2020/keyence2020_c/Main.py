n,k,s=map(int,input().split())
A=[0]*n
for i in range(k):
  A[i]=s
j=1
if s>2:
  for i in range(k,n):
    A[i]=s-1
else:
  for i in range(k,n):
    A[i]=s+1
A=[str(i) for i in A]
print(' '.join(A))