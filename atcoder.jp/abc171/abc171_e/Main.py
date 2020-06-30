def xsum(A):
    total=0
    for i in range(len(A)):
        total^=A[i]
    return total

n=int(input())
A=list(map(int,input().split()))
B=[0]*n
total=xsum(A)
for i in range(n):
    B[i]=total^A[i]
B_str=[str(i) for i in B]
print(' '.join(B_str))