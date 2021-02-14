ACGT = ['A', 'C', 'G', 'T']
S = list(input())
cnt = 0
ans = 0
for i in S:
    if i in ACGT:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)