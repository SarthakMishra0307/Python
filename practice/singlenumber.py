nums = [4,1,2,4,2]
numset = {}
for i in nums:
    numset[i] = numset.get(i,0) + 1
x= list(numset.keys())

for i in numset:
    if (numset.get(i) == 1):
        temp = i
        break
print(temp)


# print(numset)
# print(numset.get(1))
