def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int,input().split())
    X.append(x)
    Y.append(y)

total = 0
for i in range(n):
    for j in range(n):
        total += ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)**0.5

print(total/n)

