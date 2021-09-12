while True:
    try:
        num = int(input("please enter the dividend"))
        div = int(input("please enter the divisor"))
        ans= num/div
        print(ans)
        # break
        print(type(ans))
    except:
        print("please enter a non-zero input")
    finally:
        n=1
        print(f"Attempted input:{n}")
        
    