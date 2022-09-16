n = 3
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j<i :
            print(" ",end="")
        elif j>=i:
            print("*",end="")
    print("")