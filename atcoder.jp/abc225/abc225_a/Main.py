s = input()

s_set = set([i for i in s])

if len(s_set) == 3:
  print(6)
elif len(s_set) == 2:
  print(3)
else:
  print(1)
