from collections import deque

h, w, n = map(int, input().split())
g = list()
for i in range(h):
    g.append(list(input()))
time = [[-1 for _ in range(w)] for _ in range(h)]
chk = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if g[i][j] == 'S':
            s = [i, j]
            time[i][j] = 0
cheese = [0] * n
hitpoint = 1
next = [[-1, 0], [0, -1], [1, 0], [0, 1]]
stack = deque()
stack.append(s)
while stack:
    '''
    for i in range(h):
        print(time[i])
    '''
    y, x = stack.popleft()
    #print(cheese, hitpoint)
    if hitpoint == n+1:
        print(time[y][x])
        exit()
    for i, j in next:
        if 0 <= y+i < h and 0 <= x+j < w and g[y+i][x+j] != 'X' and chk[y+i][x+j] == 0:
            #print('searching y = {}, x = {}'.format(y + i, x + j))
            time[y+i][x+j] = time[y][x] + 1
            chk[y+i][x+j] = 1
            stack.append([y+i, x+j])
            if g[y+i][x+j] != 'X' and g[y+i][x+j] != '.' and g[y+i][x+j] != 'S' and int(g[y+i][x+j]) <= hitpoint and cheese[int(g[y+i][x+j]) - 1] == 0:
                cheese[int(g[y+i][x+j]) - 1] = 1
                hitpoint += 1
                stack = deque()
                stack.append([y+i, x+j])
                chk = [[0 for _ in range(w)] for _ in range(h)]
                break
