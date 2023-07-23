s = input()

for i in range(len(s)):
  if s[i].isupper():
    print(i + 1)
    exit()
