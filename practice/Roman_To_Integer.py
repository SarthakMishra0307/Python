dict = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
s = "IV"
num = 0
p0 = 0
try:
    while p0 <= len(s):
        if s[p0] == 'I':
            if s[p0 + 1] == 'V':
                num += 4
                p0 += 2
                continue
            if s[p0 + 1] == 'X':
                num += 9
                p0 += 2
                continue
        if s[p0] == 'X':
            if s[p0 + 1] == 'L':
                num += 40
                p0 += 2
                continue
            if s[p0 + 1] == 'C':
                num += 90
                p0 += 2
                continue
        if s[p0] == 'C':
            if s[p0 + 1] == 'D':
                num += 400
                p0 += 2
                continue
            if s[p0 + 1] == 'M':
                num += 900
                p0 += 2
                continue
        else:
            num += dict[s[p0]]
            p0 += 1
except:
    num += dict[s[p0]]
    p0 += 1


print(num)