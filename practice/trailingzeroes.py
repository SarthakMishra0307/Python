nums = [3,0,5,0,1,2]
temp = 0 
# for j in range(len(nums)):
#     for i in range(len(nums)-1):
#         if nums[i] == 0:
#             temp = nums[i+1]
#             nums[i] = temp
#             nums[i+1] = 0
for i in nums:
    if i == 0 :
        nums.remove(i)
        nums.append(i)

print(nums)
