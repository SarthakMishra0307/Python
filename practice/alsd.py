nums = [1,1,1,3,3,4,3,2,4,2]
dic = {}
for i in range(len(nums)):
    dic[nums[i]] = dic.get(nums[i],0) + 1  
for i in dic:
    if dic[i] >= 2:
        print(True)
        break
print(False)