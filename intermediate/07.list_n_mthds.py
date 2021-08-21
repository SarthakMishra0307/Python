marks = [3,44,6,86,235,42,13,90,12.1212,'hello']
print(marks[2])

# inmutable
a = 'jim'
b = a
a = 'tim'
print(a)
print(b)


sub = ['che', 'mec', 'phy', 'ece']
topics = sub 
print(topics)
topics[2] = 'pel'
# mutable
print(topics)
print(sub)


print(len(topics))
# print(max(sub))
# print(min(marks))

# for sorting
print(sorted(sub, reverse=True))

# join element between strings

name = ['Chandler', 'Muriel', 'Bing']
print('-'.join(name))
# gives error if contains anything other than string
# name = ['Chandler', 'Muriel', 'Bing', 23]


# append method
# ps. add an element to the end of a list.
quote = ['we were on a break']
quote.append('no we weren\'t')
print(quote)





