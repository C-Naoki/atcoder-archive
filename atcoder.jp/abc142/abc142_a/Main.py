n = int(input())
cnt = 0
for i in range(n):
  if (i + 1) % 2 == 1:
    cnt += 1
print(cnt/n)
