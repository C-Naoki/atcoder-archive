N = int(input())
P = list(map(int, input().split()))

if N == 1:
  print(0)
  exit()

max_power_except_first = max(P[1:])

if P[0] <= max_power_except_first:
    print(max_power_except_first - P[0] + 1)
else:
    print(0)
