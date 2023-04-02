dict = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
s = "IV"
num = 0

for i in range(len(s)):
    try:
        if s[i+1] == 'V' and s[i] == 'I':
            count += 4
            continue
        if s[i+1] == 'X' and s[i] == 'I':
            count += 9
            continue
        if s[i+1] == 'L' and s[i] == 'X':
            count += 40
            continue
        if s[i+1] == 'C' and s[i] == 'X':
            count += 90
            continue
        if s[i+1] == 'D' and s[i] == 'C':
            count += 400
            continue
        if s[i+1] == 'M' and s[i] == 'C':
            count += 900
            continue
    except:
        num += dict[s[i]]
        continue

    num += dict[s[i]]
print(num)