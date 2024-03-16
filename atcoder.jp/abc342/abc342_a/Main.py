s = input()

s0 = s[0]
index_ls = list()
for i in range(len(s)):
  if s[i] != s0:
    index_ls.append(i)

print(index_ls[0] + 1 if len(index_ls) == 1 else 1)
