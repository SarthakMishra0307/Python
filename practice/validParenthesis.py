s = "()[{}]"
flag = True

brack_s = ["(", "{", "["]
brack_e = [")" , "}" , "]"]

arr = []
for i in range(len(s)):
    if s[i] in brack_s:
        arr.append(s[i])
    if s[i] in brack_e:
        if not arr :
            flag = False
            break
        elif (arr.pop() + s[i]) in ["()", "[]" , "{}"]:
            pass
        else:
            flag = False
            break

# print(arr)
print(flag)

