dic_s = {}
dic_t = {}
isIsomrophic = "false"
s = "abbab"
t = "bbaab"

for i in range(len(s)):
    dic_s[s[i]] = dic_s.get(s[i],"") + i

for i in range(len(t)):
    dic_t[t[i]] = dic_t.get(t[i],0) + i

print(dic_s)
print(dic_t)

# # list for keys
# s_Key_value = list(dic_s.keys())
# t_Key_value = list(dic_t.keys())

# # list for values
# s_value = list(dic_s.values())
# t_value = list(dic_t.values())
 

# if len(s_Key_value) == len(t_Key_value):
#     if s_value == t_value:
#         isIsomrophic = "true"


# print(s_value)
# print(t_value)

# print(s_Key_value)
# print(t_Key_value)

# print(isIsomrophic)