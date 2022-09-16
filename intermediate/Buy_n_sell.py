prices = [7,1,5,3,6,4]
low_buy = prices[0]
high_buy = prices[1]
high_sell = 0
temp = 0
# while(low_buy < high_buy and high_buy != prices[-1]):
    for i in range(len(prices)):
        if prices[i] <= low_buy:
            low_buy = prices[i]
            temp = i+1
    if temp == len(prices):
        print(0)
    for i in range(temp, len(prices)):
        if prices[i] >= high_sell:
            high_sell = prices[i]
print(high_sell-low_buy)
print(low_buy)
print(high_sell)
    
