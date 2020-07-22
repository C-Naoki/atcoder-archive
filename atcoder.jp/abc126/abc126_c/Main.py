import math

def f(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += 1
    return max(cnt,1)

n, k = map(int,input().split())

cnt = f(k)
ans = 0
num = n
for i in range(n):
    while cnt != 0 and k / (i+1) <= 2**(cnt - 1):
        cnt -= 1
    ans += (1 / num)*math.pow(0.5,cnt)
print(ans)
