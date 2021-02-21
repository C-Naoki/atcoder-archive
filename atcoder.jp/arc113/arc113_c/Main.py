s = list(input())
D = list()
prev = '0'
for i in range(len(s)):
    if len(D) > 0:
        if D[len(D) - 1][0] == s[i]:
            #print(D)
            D[len(D) - 1][1] -= 1
    if s[i] == prev and (len(D) == 0 or D[len(D) - 1][0] != s[i]):
        D.append([s[i], len(s) - i - 1])
    prev = s[i]
ans = 0
for j in D:
    ans += j[1]
print(ans)