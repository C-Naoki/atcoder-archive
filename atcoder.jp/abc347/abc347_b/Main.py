s = input()
n = len(s)

ans = set()
for i in range(1, n):
  for j in range(n - i + 1):
    ans.add(s[j : j + i])

print(len(ans) + 1)
