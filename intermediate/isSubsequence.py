# arr = []
# s_arr = []
# a1= 0
# a2=0
# isSub = False
s = "ab"
t = "baab"
# for i in range(len(s)):
#     s_arr.append(s[i])

# for i in range(len(t)):       
#     if t[i] in s:
#         # if t[i] not in arr:
#             arr.append(t[i])
#     else:
#         arr.append("")
#         arr.remove("")
i = 0
j = 0
while i< len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    i+=1
if i == len(s):
    isSub = True
# else 

# print(x)
print(arr)
print(s_arr)
print(isSub)
