A, B = map(int, input().split())

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in board:
  if (A in row) and (B in row):
    if abs(row.index(A) - row.index(B)) == 1:
      print("Yes")
      exit()
print("No")