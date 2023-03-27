import math
obs_value = [2,5,6,8,2,3]
def softmax(arr):
    summation = 0
    for i in range(len(arr)):
        summation += math.exp(arr[i])

    print(summation)
    prob = [round(math.exp(arr[i])/summation,4) for i in range(len(arr))]
    return prob

    
values= softmax(obs_value)
print(values)
