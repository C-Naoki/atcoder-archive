x, k, d = map(int,input().split())
if x < 0:
    m = 1
else:
    m = 0
x = abs(x)
mod = x%d
ans = x//d
if ans < k:
    if (k - ans)%2 == 0:
        if m == 0:
            print(abs(mod))
        else:
            print(abs(-mod))
    else:
        if m == 0:
            print(abs(mod - d))
        else:
            print(abs(-mod + d))
else:
    if m == 0:
        print(abs(x - k*d))
    else:
        print(abs(-x + k*d))