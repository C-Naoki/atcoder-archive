data = """
tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
"""

data_lines = data.strip().split("\n")
data_dict = {line.split()[0]: int(line.split()[1]) for line in data_lines}

s = input()

print(data_dict[s])
