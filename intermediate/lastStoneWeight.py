stones = [2,7,4,1,8,1]
num = 0
num_2  = 0
# index_num = 0
# index_num2 = 0
for i in range(1):
    num_index = stones.index(max(stones))
    num2_index = stones.index(max(stones))
    stones.pop(num2_index)
    # num = stones[num_index]
    print(num2_index)
    print(num_index)
    # if num == num_2:
    #     continue
    # if num > num_2:
    #     stones[num_index] = num - num_2
    # stones.pop(num_index)
print(stones)