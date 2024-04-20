s = input()

atcoder_ls = ["ABC" + f"{i}".zfill(3) for i in range(1, 350)]

if s == "ABC316":
  print("No")
  exit()
print("Yes" if s in atcoder_ls else "No")
