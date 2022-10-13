nums = [3,2,4]
target = 6

prevMap = {}

for i,n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
        return [prevMap[diff], i]
    prevMap[n] = i



# list((nums.index(nums[i]),nums.index(nums[j])))











# except:
#     print("out of range")

# for i in range(len(nums)-1):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i,j])