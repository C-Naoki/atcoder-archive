n = int(input())
s, t = map(str,input().split())
ans = ['0']*(2*n)
for i in range(2*n):
    if i % 2 == 0:
        ans[i] = s[i//2]
    else:
        ans[i] = t[i//2]
print(''.join(ans))