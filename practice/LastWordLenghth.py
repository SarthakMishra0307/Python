s= "a"
count = 0

p1 = len(s)

while p1 != 0:
    if s[p1-1] == " ":
        if p1 == len(s):
            p1 -= 1
            continue
        if s[p1] != " ":
            break
        p1 -= 1
        continue
    else:
        count += 1
        p1 -= 1
        continue

print(count)
