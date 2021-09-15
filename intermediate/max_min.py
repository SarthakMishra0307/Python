arr = [10,9,8,11,13,1,7]
min = 0 
max = 0
for x in range(0,(len(arr)-1)):
    if arr[x] < arr[x+1]:
        min = arr[x]
    elif arr[x] > arr[x+1]:
        max = arr[x]
    else:
        continue

print(min)
print(max)
