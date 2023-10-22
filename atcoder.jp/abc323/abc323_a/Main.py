s = input()

for i in range(1, len(s), 2):
  if s[i] == "1":
    print("No")
    exit()
print("Yes")
