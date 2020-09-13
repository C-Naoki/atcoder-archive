import itertools
s = int(input())
if s < 3:
    print(0)
    exit()

l = [1]*(s - 2)
total = 0
three_cnt = s // 3

for i in range(three_cnt):
    total += l[s - 3 - (i*3)]
    for j in range(s - 3):
        l[j + 1] += l[j]
print(total % ((10 ** 9) + 7))