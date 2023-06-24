N = int(input())
people = []
ages = []

for _ in range(N):
    name, age = input().split()
    age = int(age)
    people.append(name)
    ages.append(age)

min_age_idx = ages.index(min(ages))

for i in range(N):
  print(people[(i+min_age_idx)%N])