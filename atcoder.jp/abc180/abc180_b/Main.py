n = int(input())
X = list(map(int,input().split()))
m = 0
for i in range(n):
    m += abs(X[i])
y = 0
for i in range(n):
    y += X[i] ** 2
c = 0
for i in range(n):
    c = max(c,abs(X[i]))
print(m)
print(y ** 0.5)
print(c)