a = [1,4,6,2,5,7]
temp = 0
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j-1]>a[j]:
            temp = a[j-1]
            a[j-1] = a[j]
            a[j] = temp
print(a)

