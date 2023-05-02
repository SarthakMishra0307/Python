# reading the contents of file and writing it in the reverse order in a new file

# readlines() will return a list containg the lines of file as each object
# so will iterate it in reverse order

# with open('text.txt','r+') as reader:
#     content = reader.readlines()
#     with open('text2.txt','a') as writer:
#         for line in range(len(content)):
#             writer.write(content.pop())


# or use the reversed() method

# with open('text.txt','r+') as reader:
#     content = reader.readlines()
#     with open('text2.txt', 'w') as writer:
#         for line in reversed(content):
#             writer.write(line)