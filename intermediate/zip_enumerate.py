# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

# points = []

# for point in zip(labels,x_coord,y_coord,z_coord):
#     points.append("{}: {}, {}, {}".format(*point))
# print(points)
# for point in points:
#     print(point)


cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)
