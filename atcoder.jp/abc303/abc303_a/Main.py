N = int(input())
s = input()
t = input()

for s_i, t_i in zip(s, t):
  if s_i == t_i:
    continue
  elif (s_i == "l" and t_i == "1") or (s_i == "1" and t_i == "l"):
    continue
  elif (s_i == "o" and t_i == "0") or (s_i == "0" and t_i == "o"):
    continue
  else:
    print("No")
    exit()
print("Yes")
