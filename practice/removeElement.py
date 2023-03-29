nums = [3,3]
val =3
count = 0
l = 0 
r = len(nums)-1
while l <= r:
    if nums[l] == val:
        nums[l], nums[r] = nums[r], nums[l]
        r -= 1
        count += 1
    else:
        l += 1
print(nums)
print(len(nums)-count)