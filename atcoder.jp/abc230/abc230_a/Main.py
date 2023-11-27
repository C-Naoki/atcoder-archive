n = int(input())

chk = (n >= 42)

if n < 10:
  print(f"AGC00{n}")
else:
  print(f"AGC0{n + chk}")
