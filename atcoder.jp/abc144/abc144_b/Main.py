N = int(input())
s = 'No'
for i in range(1,10):
  for j in range(1,10):
    if i * j == N:
      s = 'Yes'
print(s)
