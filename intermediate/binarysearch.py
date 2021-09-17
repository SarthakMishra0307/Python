key = 0
beg = 0 

arr = [5,7,2,4,1,0,9,8,3]
arr.sort()

end = len(arr)
mid = (beg+end)/2


for search in range(0,end):
    if key == arr[mid]:
        print(f"Number found at the {mid}th position")
    break

