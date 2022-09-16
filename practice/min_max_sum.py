def miniMaxSum(arr):
    # Write your code here
    minSum = 0
    maxSum = 0
    arr.sort()
    for i in range(len(arr)-1):
        minSum += arr[i]
        maxSum += arr[i+1]
    return print(minSum, maxSum)

arr = [1,2,3,4,5]
miniMaxSum(arr)