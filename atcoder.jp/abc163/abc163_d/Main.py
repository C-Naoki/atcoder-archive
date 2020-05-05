n,k = map(int,input().split())
total = 0
for i in range(k,n+2):
    m = i*(i-1)//2
    M = i*n-(i*(i-1))//2
    total += M - m + 1
print(total % (10**9 + 7))