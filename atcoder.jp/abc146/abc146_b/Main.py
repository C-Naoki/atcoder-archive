n = int(input())
s = list(input())
'''
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(len(s)):
    s[i] = alp[(int(alp.index(s[i])) + n) % len(alp)]

print(''.join(s))
'''

for i in range(len(s)):
    s[i] = chr((ord(s[i]) + n - 65)%26 +65)

print(''.join(s))