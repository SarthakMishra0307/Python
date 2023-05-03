try:
    with open('hello.txt','r') as f:
        f.read()
# except FileNotFoundError:
#     print("First create the file")

except Exception as e:
    print(e)



# finally block will always run NO MATTER if the try block catches
# an error or not, or due to various reasons

finally:
    # with open('hello.txt','w+') as f:
    #     f.read()
    print("Cleaning up the resources")