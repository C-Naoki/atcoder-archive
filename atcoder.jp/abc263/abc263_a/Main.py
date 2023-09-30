import collections

symbols = collections.Counter(list(map(int, input().split())))

if len(symbols) == 2 and 2 <= list(symbols.values())[0] <= 3:
  print("Yes")
else:
  print("No")
