
arr = list(range(10,111,10))
print(arr)

x = 0
for i in range(len(arr)//2):
    last = arr.pop(-1)
    arr.insert(x, last)
    x+=2
    
print(arr)