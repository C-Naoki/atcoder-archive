n = int(input())
s = input()

ans = "No"
for s_i in s:
  if s_i == "x":
    ans = "No"
    break
  elif s_i == "o":
    ans = "Yes"
print(ans)
