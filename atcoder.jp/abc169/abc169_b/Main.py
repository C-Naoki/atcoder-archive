n = int(input())
A = list(map(int,input().split()))
total = 1
count = 0
for i in range(n):
    total *= A[i]
    if total > 10**18:
        count += 1
        break

if 0 in A:
    print('0')
elif count == 1:
    print('-1')
else:
    print(total)