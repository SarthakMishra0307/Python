while left < len(nums):
    if right == len(nums)-1 :
        left += 1
    if right != len(nums) - 1:
        x= nums[slice(right,i)]
        right += 1
    print(x)