s = input()
k = int(input())
n = len(s)
l = [1]*n
'''
S = set(s)
n1 = len(s)
n2 = len(S)
l = [0]*n1

for i in range(n2):
    for j in range(n1):
        temp = 0
        chk = 0
        if s[i] == s[j]:
            l[chk] += 1
        else:
            chk += 1
'''

chk = 0
temp = 0
for i in range(n-1):
    if s[i+1] == s[i]:
        l[chk] += 1
    else:
        chk += 1

if s[0] == s[n-1]:
        temp = 1

memo = 0
edge = 0
ans = 0
for i in range(n-1,-1,-1):
    if l[i] != 1 and memo == 0 and temp == 1:
        memo += 1
        edge = i
    ans += k*(l[i]//2)

if temp == 1 and edge != 0: 
    if (l[0] + l[edge]) % 2 == 0 and l[0] % 2 == 1:
        ans += k-1
elif temp == 1:
    if l[0] % 2 == 1:
        ans += k//2
if n == 1:
    ans = k//2

print(ans)
