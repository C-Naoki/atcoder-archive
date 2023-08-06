s = input()
 
cnt = 0
for s_i in s:
  if s_i == "w":
    cnt += 2
  elif s_i == "v":
    cnt += 1
print(cnt)