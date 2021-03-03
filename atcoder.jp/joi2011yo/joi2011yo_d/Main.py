n = int(input())
L = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(n+1)]
dp[1][L[0]] = 1
for i in range(1, n):
    for j in range(21):
        if dp[i][j] != 0 and L[i] != 0:
            if j + L[i] <= 20:
                dp[i+1][j + L[i]] += dp[i][j]
            if j - L[i] >= 0:
                dp[i+1][j - L[i]] += dp[i][j]
        elif L[i] == 0:
            dp[i+1][j] = 2 * dp[i][j]

print(dp[n-1][L[n-1]])