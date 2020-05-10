s = [i for i in input()]
t = [i for i in input()]
s.append(t[-1])
if s == t:
    print('Yes')
else:
    print('No')
