s = input()

ans = list()
for f_n, l_n in zip(s[0::2], s[1::2]):
  ans.append(l_n)
  ans.append(f_n)

print(''.join(ans))
