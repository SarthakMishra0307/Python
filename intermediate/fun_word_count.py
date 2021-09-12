def word_count(sent, keyword):
    discrete = []
    count = 0
    discrete = sent.split()
    for i in discrete:
        if i == keyword:
            count += 1
    return count

s = str(input("please enter the sentence"))
word = str(input("enter the keyword you want to search"))
print(word_count(s, word))