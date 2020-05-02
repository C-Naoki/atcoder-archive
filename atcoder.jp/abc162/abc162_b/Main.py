n = int(input())
total = 0
for i in range(n+1):
  if i % 3 != 0 and i % 5 != 0:
    total += i
    
print(total)