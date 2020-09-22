s = input()
S = set(s)
if len(S) != 2:
    print('No')
    exit()
else:
    for i in range(4):
        if s.count(s[i]) != 2:
            print('No')
            exit()

print('Yes')

