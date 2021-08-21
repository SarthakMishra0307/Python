a = {'india':'+91', 'USA':'+1', 'me':{'breakfast':'paneer', 'lunch':'chips', 'dinner':'chaap'}}
print(a['india'])

print(a['me']['lunch'])

print('china' in a)

print(a.get("dilithium", 'There\'s no such element!'))

a['Britain'] = '+21'
a[401] = 'Kebab'
# print(a['Britain'])
# del a[401]


# b and a is a pointer here thats why change is also happening in a
# b = a 
# del b[401]
# print(a)

# iss tarike se aisa nahi hoga
b = a .copy()
del b[401]
print(a)

a.update({})

print(a.keys())