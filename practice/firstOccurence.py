haystack = "leetcode"
needle = "leet"
p00=0
p01=0
p1=0
idx=1e5
while(p00<len(haystack)-len(needle)+1):
    while(p1<len(needle) and p01<len(haystack) and haystack[p01]==needle[p1]):
        p01+=1
        p1+=1
    if(p1==len(needle)):
        idx=p00
        break
    p00+=1
    p01=p00
    p1=0
if idx==1e5:
    print(-1)
else:
    print(idx)