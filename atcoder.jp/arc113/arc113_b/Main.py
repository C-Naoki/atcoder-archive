a, b, c = map(int, input().split())
c %= 4
if c == 0:
    c = 4
b = b ** c
b %= 4
if b == 0:
    b = 4
a = a ** b
print(a % 10)