a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
count = 0
if w>=v:
    print('NO')
elif t*(v-w)<abs(a-b):
    print('NO')
else:
    print('YES')