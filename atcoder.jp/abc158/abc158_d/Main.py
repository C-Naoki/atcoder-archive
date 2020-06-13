from collections import deque
s=deque(list(input()))
Q=int(input())
count = 0
for i in range(Q):
    q=input()
    if q[0]=='1':
        count += 1
    elif (q[2]=='1' and count%2==0) or (q[2]=='2' and count%2==1):
        s.appendleft(q[4])
    elif (q[2]=='2' and count%2==0) or (q[2]=='1' and count%2==1):
        s.append(q[4])

if count%2==0:
    print(''.join(s))
else:
    print(''.join(reversed(s)))