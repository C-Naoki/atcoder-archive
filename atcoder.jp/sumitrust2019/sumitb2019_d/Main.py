n = int(input())
s = list(input())
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            cnt = 0
            for a in range(n):
                if s[a] == str(k) and cnt == 2:
                    ans += 1
                    break
                elif s[a] == str(j) and cnt == 1:
                    cnt += 1
                elif s[a] == str(i) and cnt == 0:
                    cnt += 1
                #print(i)
print(ans)
