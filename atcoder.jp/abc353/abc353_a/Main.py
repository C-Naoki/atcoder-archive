n = int(input())
H = list(map(int, input().split()))

for i in range(1, n):
  if H[0] < H[i]:
    print(i + 1)
    exit()
print(-1)
