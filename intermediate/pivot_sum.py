nums = [1,7,3,6,5,6]
pvt_no = 0
# for i in range(len(nums)):
#     back_Sum = 0
#     frnt_Sum = 0
#     for j in range(len(nums)):
#         if i==j:
#             continue
#         elif i > j:
#             back_Sum += nums[j]
#         elif i < j: 
#             frnt_Sum += nums[j]
#     if frnt_Sum == back_Sum:
#         pvt_no = i
#         break
#     else:
#         pvt_no = -1
#         continue
# print(pvt_no)
# return pvt_no


# O(n*2) time complexity
lsum = 0
arr_sum = 0
for i in range(len(nums)):
    arr_sum += nums[i]
for i in range(arr):
    arr_sum -= nums[i]
    if lsum == arr_sum:
        break
    lsum += nums[i]

    


