cost = [1,100,1,1,1,100,1,1,100,1]
x = 0 
cost1 = cost[0]
# cost2 = cost[1]
for i in range(len(cost)):
    
    x= min(cost[i],cost[i+1])
    cost1 += x
    # else:
    #     continue

print(x)
