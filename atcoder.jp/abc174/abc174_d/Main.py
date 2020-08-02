n = int(input())
C = input()
chk = 0
for i in range(n):
    if C[n-1-i] == 'R':
        chk = n-1-i
        break
cnt = 1
for i in range(chk):
    if C[i] == 'R':
        cnt += 1
ans = 0
for i in range(cnt):
    if C[i] == 'W':
        ans += 1
if 'R' not in C:
    print(0)
else:
    print(ans)