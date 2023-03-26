testcase = int(input())
for _ in range(testcase):
    num_len = int(input())
    num = str(input())
    for i in range(num_len):
        l = 0
        r = num_len - 1
        if l == r:
            print(num[l])
        if num[l] == 1 and num[r] == 0 or num[l] == 0 and num[r] == 1:
            l += 1
            r -= 1
            
            print(num)
        # else:
        #     print(num)
# print(num[1])
# print(num[1:3])
    print(num)