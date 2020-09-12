s = input()
t = input()
cnt = 0
ans = 0
while cnt < len(s) - len(t) + 1:
    chk = 0
    for i, j in zip(range(cnt,cnt+len(t)),range(len(t))):
        if s[i] == t[j]:
            chk += 1
    ans = max(ans,chk)
    cnt += 1

print(len(t) - ans)