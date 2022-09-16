def intersection3(lst1, lst2, list3):
    return list(set(lst1) & set(lst2) & set(list3))

def intersection2(lst1, lst2 ):
    return list(set(lst1) & set(lst2))

C = [7, 8, 9, 18, 20, 21, 25, 26, 27, 31, 32, 34, 35, 36, 40, 43, 45, 47, 53, 58, 62, 67, 68, 71, 72, 74, 75, 76,
80, 81, 82, 90, 93, 95, 97, 99]
F = [1, 7, 10, 13, 16, 22, 24, 29, 30, 32, 34, 39, 40, 43, 44, 48, 56, 60, 65, 68, 69, 73, 77, 78, 90, 93, 94, 95,
96]
H = [5, 12, 14, 17, 20, 21, 22, 25, 28, 30, 37, 38, 39, 40, 42, 44, 57, 59, 61, 62, 67, 71, 75, 76, 77, 82, 83, 86,
87, 92, 94, 95]

Hhash =[]
Chash =[]
Fhash =[]

for i in range(1,101):
    if i not in H:
        Hhash.append(i)
    if i not in C:
        Chash.append(i)
    if i not in F:
        Fhash.append(i)


# ques 1 students who play any of the sports
print("students who play any of the sports:")
none = intersection3(Chash, Fhash, Hhash)
print(none)

# students who play all the games
print("\nstudents who play all the games")
all = intersection3(C,F,H)
print(all)



cricketAndHockey = intersection2(C,H)
cricketAndFootball = intersection2(C,F)
footballAndHockey = intersection2(F,H)


for i in all:
    if i in cricketAndHockey:
        cricketAndHockey.remove(i)
        cricketAndFootball.remove(i)
        footballAndHockey.remove(i)
    else: continue


cricketAndHockey.sort()
cricketAndFootball.sort()
footballAndHockey.sort()


print("\nStudents who play cricket and hockey but not football:")
print(cricketAndHockey)
print("\nStudents who play cricket and hockey but not football:")
print(cricketAndFootball)
print("\nStudents who play cricket and hockey but not football:")
print(footballAndHockey)




