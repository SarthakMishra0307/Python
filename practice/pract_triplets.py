def compareTriplets(a, b):
    # Write your code here
    resArr =[]
    p1 = 0
    p2 = 0
    for i,j in zip(a,b):
        if i>j:
            p1 += 1
        elif i < j:
            p2 += 1
    resArr.append(p1)
    resArr.append(p2)
    return resArr