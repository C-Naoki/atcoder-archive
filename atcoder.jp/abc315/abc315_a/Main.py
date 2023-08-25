s = input()

ans = ""
for s_i in s:
  if s_i not in ["a", "i", "u", "e", "o"]:
    ans += s_i
print(ans)
