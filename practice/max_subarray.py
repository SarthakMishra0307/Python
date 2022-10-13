nums = [-2,1,-3,4,-1,2,1,-5,4]
left = 0
right = 0
add = 0

while left != len(nums)-1:
    right += 1
    x= nums[left:right]
    if right==len(nums):
        left += 1
        right = left
    listSum = sum(x)
    if listSum >= add:
        add = listSum
    print(add)
        

    