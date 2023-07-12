n = int(input())
s = input()

st = 0
en = 0
ans = "out"
for mark in s:
    if mark == "|":
        if not st:
            st = 1
        else:
            en = 1
    if st and not en and mark == "*":
        ans = "in"
print(ans)