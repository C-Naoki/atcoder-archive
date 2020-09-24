n = int(input())
B = list(map(int,input().split()))
ans = 0
for i in range(n-2):
    ans += min(B[i],B[i+1])
print(B[0]+ans+B[n-2])