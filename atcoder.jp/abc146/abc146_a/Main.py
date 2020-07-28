s = input()
day = ['SAT','FRI','THU','WED','TUE','MON','SUN']
for i in range(7):
  if s == day[i]:
    print(i + 1)
    exit()