n = int(input())

ans = ""
for i in range(n):
  if (i + 1) % 3 != 0:
    ans += "o"
  else:
    ans += "x"
print(ans)
