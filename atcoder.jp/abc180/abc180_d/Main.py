x, y, a, b = map(int,input().split())
total = x
ans = 0
while total * a < total + b:
    if total * a >= y:
        print(ans)
        exit()
    total *= a
    ans += 1
if (y - total) % b == 0:
    ans += ((y - total) // b) - 1
else:
    ans += (y - total) // b
print(max(ans,0))