n=int(input())
A=[0]+list(map(int,input().split()))
B=[0]+list(map(int,input().split()))
C=[0]+list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

total = [0]*(n+1)
ans = [0]*(n+1)
for i in range(n+1):
    l1 = 0
    r1 = n+1
    while l1 != r1:
        mid1 = (l1 + r1)//2
        if B[i] > A[mid1]:
            l1 = mid1 + 1
            total[i]=max(total[i],mid1+total[i-1])
        else:
            r1 = mid1

for i in range(n+1):
    l2 = 0
    r2 = n+1
    while l2 != r2:
        mid2 = (l2 + r2)//2
        if C[i] > B[mid2]:
            l2 = mid2 + 1
            ans[i] = max(ans[i],total[mid2])
        else:
            r2 = mid2
print(sum(ans))
