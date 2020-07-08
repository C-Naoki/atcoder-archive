n,k,m=map(int,input().split())
A=list(map(int,input().split()))

if sum(A) + k < n*m:
    print(-1)
    exit()

ans = 0

while ans < n*m - sum(A):
    ans += 1

print(ans)