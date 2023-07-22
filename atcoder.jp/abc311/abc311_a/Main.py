n = int(input())
s = input()

chks = [0, 0, 0]
symbols = ["A", "B", "C"]
for i in range(n):
  for j, symb in enumerate(symbols):
    if s[i] == symb:
      chks[j] = 1
  if sum(chks) == 3:
    print(i + 1)
    exit()
