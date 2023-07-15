n = int(input())
s = input()

if n == 1:
  print("Yes")
else:
  bf = s[0]
  ans = "Yes"
  for s_i in s[1:]:
    if bf == s_i:
      ans = "No"
    bf = s_i
  print(ans)
