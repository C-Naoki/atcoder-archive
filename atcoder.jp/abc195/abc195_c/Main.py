n = int(input())
chk = 6
ans = 0
while (n % 10 ** chk) != n:
    ans += (10 ** chk - (10 ** (chk-3))) * ((chk-3) // 3)
    chk += 3
ans += (n - 10**(chk-3) + 1) * ((chk-3) // 3)
print(max(ans, 0))