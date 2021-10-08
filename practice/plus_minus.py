def plusMinus (arr):
    isPositive = 0
    isNegative = 0
    isZero = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            isPositive += 1
        elif (arr[i]==0):
            isZero += 1
        else:
            isNegative += 1
    isPositive, isNegative, isZero =  isPositive/len(arr) ,isNegative/len(arr) ,isZero/len(arr)
    # return print("{:.6f} \n{:.6f} \n{:.6f}".format(isPositive,isNegative,isZero))
    return print("",format(isPositive,'0.6f'),"\n",format(isNegative,"0.6f"),"\n",format(isZero,'0.6f'))

array = []
lenght_arr = int(input("Enter the lenght of arr"))
for i in range(lenght_arr):
    try:
        array.append(int(input())) 
    except:
        print("please enter a valid integer input")
plusMinus(array)



