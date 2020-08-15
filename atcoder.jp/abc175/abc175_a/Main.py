s = input()
cnt=[0]*3
j = 0
for i in range(3):
    if s[i] == 'R':
        cnt[j] += 1
    else:
        j += 1
print(max(cnt))