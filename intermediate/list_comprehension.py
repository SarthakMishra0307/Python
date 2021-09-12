# even = [(x**2) for x in range(9) if x%2 == 0]
# print(even)


# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# first_names = []
# print(first_names)



# passed = []
# scores = {
#             "Rick Sanchez": 70,
#             "Morty Smith": 35,
#             "Summer Smith": 82,
#             "Jerry Smith": 23,
#             "Beth Smith": 98
#         }
# for score in scores:
#     if scores[score]>65:
#         passed.append(score)
# print(passed)

# passed = # write your list comprehension here
# print(passed)


scores = {
            "Rick Sanchez": 70,
            "Morty Smith": 35,
            "Summer Smith": 82,
            "Jerry Smith": 23,
            "Beth Smith": 98
        }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
