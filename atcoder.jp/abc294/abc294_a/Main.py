n = int(input())
a = list(map(int, input().split()))

ans = list()
for i in range(n):
  if not a[i] % 2:
    ans.append(str(a[i]))

print(" ".join(ans))
