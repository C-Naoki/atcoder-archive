x = int(input())
yokin = 100
count = 0
while yokin < x:
    yokin = yokin*1.01
    yokin = int(yokin)
    count += 1

print(count)