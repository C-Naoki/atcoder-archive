s = input()
n = len(s)

l = 0
r = 0
ans = 0
for i in range(n):
    if '<' == s[i]:
        if r != 0:
            M = max(l,r)
            m = min(l,r)
            ans += M*(M+1)//2 + m*(m-1)//2
            r = 0
            l = 0
        l += 1
    if '>' == s[i]:
        r += 1

M = max(l,r)
m = min(l,r)
ans += M*(M+1)//2 + m*(m-1)//2
print(ans)