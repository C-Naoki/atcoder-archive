s, t, x = map(int, input().split())

if s > t:
  t += 24

print("Yes" if (s <= x < t) or (s <= x + 24 < t) else "No")
