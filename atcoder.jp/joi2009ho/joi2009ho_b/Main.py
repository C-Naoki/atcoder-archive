d = int(input())
n = int(input())
m = int(input())
D = [0]
K = list()
ans = 0
for i in range(n - 1):
    D.append(int(input()))
D.append(d)
for i in range(m):
    K.append(int(input()))
D.sort()
for i in range(m):
    left = 0
    right = n
    distance = float('inf')
    while left <= right:
        half = (left + right) // 2
        if D[half] > K[i]:
            right = half - 1
        elif D[half] < K[i]:
            left = half + 1
        else:
            distance = 0
            break
        distance = min(distance, abs(D[half] - K[i]))
        #print(distance, left, right, half, K, D)
    ans += distance
    #print(' ')
print(ans)