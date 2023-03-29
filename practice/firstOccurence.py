haystack = "leetcode"
needle = "leet"
flag = False
p0 = 0
p1 = 0
p2 = 0
while p1 != (len(haystack)-len(needle) + 1):
    p1 = p0
    while(p2<len(needle) and p1<len(haystack) and haystack[p1]==needle[p2]):
        if p2 == len(needle)-1 :
            flag = True
            break
        p1 += 1
        p2 += 1
        continue
    else:
        p0 += 1
        p2 = 0
        continue
if flag:
    print(0)
else:
    print(-1)


# p00=0
# p01=0
# p1=0
# idx=1e5
# while(p00<len(haystack)-len(needle)+1):
#     while(p2<len(needle) and p1<len(haystack) and haystack[p1]==needle[p2]):
#         p01+=1
#         p1+=1
#     if(p1==len(needle)):
#         idx=p00
#         break
#     p00+=1
#     p01=p00
#     p1=0
# if idx==1e5:
#     print(-1)
# else:
#     print(idx)