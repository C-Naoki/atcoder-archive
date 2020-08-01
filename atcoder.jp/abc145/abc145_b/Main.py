n = int(input())
s = input()
if n%2==0 and s[0:(n+1)//2] == s[(n+1)//2:]:
  print('Yes')
else:
  print('No')