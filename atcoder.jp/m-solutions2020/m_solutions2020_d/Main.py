n = int(input())
A = list(map(int,input().split()))
chk = [0]*(n-1)
for i in range(n-1):
    if A[i + 1] > A[i]:
        chk[i] = 2
    elif A[i + 1] < A[i]:
        chk[i] = 0
    else:
        chk[i] = 1
c = 0
money = 1000
stock = 0
for i in range(n-1):
    if chk[i] == 2 and c == 0:
        stock = money//A[i]
        money -= stock*A[i]
        c = 1
    elif chk[i] == 0 and c == 1:
        money += stock*A[i]
        stock = 0
        c = 0
    if 2 not in chk[i:]:
        money += stock*A[i]
        stock = 0
        break
money += stock*A[n-1]
print(money)