# s = "left**cod*e"
# s = "erase*****"

new_s = ""
arr= []
for i in range(len(s)):
    if s[i] == "*":
        arr.pop()
    else:
        arr.append(s[i])

for i in range(len(arr)):
    new_s += arr[i]
