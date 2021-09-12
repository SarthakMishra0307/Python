# sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# for i in sentence():
#     print(i)


# for i in range(5,31,5):
#     print(i)


# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []
# for name in names:
#     usernames.append(name.lower())
# print(usernames)

# for i in range(len(names)):
#     x = names[i].lower()
#     y = x.replace(" ", "_")
#     usernames.append(y)
#     # usernames.append(names[i].lower().replace(" ", "_"))
# # print(usernames)
# print(usernames)

# word_counter = {}
# book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
# for word in book_title:
#     if word not in book_title:
#         word_counter[word] = 1
#     else:
#         word_counter[word] += 1


# cast = {           "Jerry Seinfeld": "Jerrasdy Seinfeld",
#     "Julia Louis-Dreyfus": "Elasadine Benes",
#     "Jason Alexander": "Georgeasd Costanza",
#         "Michael Richards": "Cosmogr Kramer"
#     }

# for key in cast:
#     print(key)

# for key, value in cast.items():
#     print( 'Actor: {}    Role: {}'.format(key, value))


result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for item in basket_items:
    if item in fruits:
        result += basket_items[item]
print(result)