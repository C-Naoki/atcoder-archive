s = input()
cnt = 0
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        cnt += 1
print(cnt)