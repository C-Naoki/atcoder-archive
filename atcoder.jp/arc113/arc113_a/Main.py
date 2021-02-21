k = int(input())
ans = 0
for i in range(1, k+1):
    for j in range(1, (k+1)//i + 1):
        for l in range(1, (k+1)//(i*j) + 1):
            if i * j * l <= k:
                ans += 1
print(ans)