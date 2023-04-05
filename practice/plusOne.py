digits = [5,9,9,9]

num = 0

for i in digits:
    num = (num *10) + i
num = str(num+1)
digits = []
for i in range(len(num)):
    digits.append(num[i])

print(digits)