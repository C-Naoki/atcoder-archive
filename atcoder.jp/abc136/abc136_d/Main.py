s = input()
n = len(s)
cntr = 0
cntl = 0
ansr = [0]*n
for i in range(n):
    if s[i] == 'R':
        cntr += 1
    if s[i] == 'L':
        ansr[i] += cntr//2
        ansr[i-1] += (cntr - ansr[i])
        cntr = 0

ansl = [0]*n
for i in range(n-1,-1,-1):
    if s[i] == 'L':
        cntl += 1
    if s[i] == 'R':
        ansl[i] += cntl//2
        ansl[i+1] += (cntl - ansl[i])
        cntl = 0

ans = [0]*n
for i in range(n):
    ans[i] = ansl[i] + ansr[i]

ans_str = [str(i) for i in ans]
print(' '.join(ans_str))