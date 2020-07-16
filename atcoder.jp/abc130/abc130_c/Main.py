w, h, x, y = map(int,input().split())
if w/2 == x and h/2 == y:
    cnt = 1
else:
    cnt = 0

print(h * w / 2, cnt)