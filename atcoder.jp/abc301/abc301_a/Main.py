n = int(input())
s = input()

t_cnt = 0
a_cnt = 0
for s_i in s:
  if s_i == "T":
    t_cnt += 1
  else:
    a_cnt += 1
    
if a_cnt > t_cnt:
  print("A")
elif a_cnt < t_cnt:
  print("T")
else:
  if s[-1] == "A":
    print("T")
  else:
    print("A")
