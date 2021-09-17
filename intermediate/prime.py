number = int(input("Please enter the number :"))
# count  = 0
prime = True
x= 0 
if number % 2 == 0:
    x= (number+1)//2
elif number % 2 == 1:
    x= number//2

for i in range(2,x+1):
    if number%i == 0:
        # count = count +1
        prime =False

if prime:
    print("It is a prime no.")
else:
    print("It is not a prime")
    