s = "bbbab"
dic = {}
for i in range(len(s)):
    dic[s[i]] = dic.get(s[i],0) + 1


new_s = ""

# for i in range(max(dic[x])):
# new_s += max(dic, key= lambda x: dic[x])

# print(new_s)
s = max(dic, key= lambda x: dic[x])
print(s)