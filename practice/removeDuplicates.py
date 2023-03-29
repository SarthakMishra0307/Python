nums = [0,0,1,1,1,2,2,3,3,4]
count = 1
temp = 0
l = 0
r = 1

for i in range(len(nums)-1):
    if nums[l] == nums[r]:
        pass
    else:
        l += 1
        temp = nums[r]
        nums[r] = nums[l]
        nums[l] = temp
        count = count + 1
        if r == len(nums)-1 :
            break
    r += 1
    
print(nums)
print(count)
