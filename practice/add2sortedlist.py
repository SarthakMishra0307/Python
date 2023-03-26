n1 = [1,5,7,11,13]
n2 = [2,4,12,13,14]

lst= []
l,r = 0,0 
while l<len(n1) and r<len(n2):
    if n1[l] < n2[r]:
        lst.append(n1[l])
        l += 1
    else:
        lst.append(n2[r])
        r += 1

while l < len(n1):
    lst.append(n1[l])
    l += 1
while r < len(n2):
    lst.append(n2[r])
    r += 1

print(lst)