from collections import Counter

s = input()
a = [0]
mod = 2019

for i,j in enumerate(s[::-1]):
    a.append(a[-1] + int(j)*pow(10,i,mod))
    a[-1] %= mod
b = Counter(a)

ans = 0
for i in b.values():
    ans += i*(i-1)//2
print(ans)