import collections
r, c = map(int, input().split())
s = list(map(int, input().split()))
g = list(map(int, input().split()))
C = list()
for i in range(r):
    C.append(list(input()))
stack = collections.deque()
stack.append(s)
chk = [[0 for _ in range(c+1)] for _ in range(r+1)]
ans = [[0 for _ in range(c+1)] for _ in range(r+1)]
ans[s[1]][s[0]] = 0
chk[s[1]][s[0]] = 1
while stack:

    y, x = stack.popleft()
    #print('y is {} x is {}'.format(y, x))
    if y == g[0] and x == g[1]:
        print(ans[y][x])
        exit()
    for i in range(-1,2,2):
        #print('now searching y is {} x is {}'.format(y+i, x))
        #print('now searching y is {} x is {}'.format(y, x+i))
        if 0 < y+i <= r and C[y+i-1][x-1] == '.' and chk[y+i][x] == 0:
            stack.append([y+i, x])
            chk[y+i][x] = 1
            ans[y+i][x] = (ans[y][x] + 1)
        if 0 < x+i <= c and C[y-1][x+i-1] == '.' and chk[y][x+i] == 0:
            stack.append([y, x+i])
            chk[y][x+i] = 1
            ans[y][x+i] = (ans[y][x] + 1)