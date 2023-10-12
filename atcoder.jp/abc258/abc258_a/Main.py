k = int(input())

if k >= 60:
  print(f"22:{str(k % 60).zfill(2)}")
else:
  print(f"21:{str(k).zfill(2)}")
