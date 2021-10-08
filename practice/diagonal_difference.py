rows,columns = int(input("Enter row ")),int(input("Enter column "))
# col_arr = []

# for i in range(rows):
#     row_arr = []

#     for j in range(columns):
#         temp = input("["+str(i+1)+ "x" +str(j+1)+"]  - ")
#         row_arr.append(temp)
#     col_arr.append(row_arr)

# print(col_arr)


# matrix = [[0 for i in range(columns)] for j in range(rows)]
# for i in range(rows):
#     for j in range(columns):
#         try:
#             temp= int(input("["+str(i+1)+ "x" +str(j+1)+"]  - "))
#             matrix[i][j] = temp
#         except:
#             print("wrong input")
#             j -= 1
# print(matrix)

matrix = [[11, 2, 4], [9, 5, 6], [10, 8, -12]]

fr_sum=0
bc_sum = 0

for i in range(0,rows):
    fr_sum += matrix[i][i]
    for k in range(rows-1,1,-1):
            bc_sum += matrix[i][k-i]

# EAAZZYY
# for i in range(rows):
#     fr_sum += matrix[i][i]     
#     bc_sum += matrix[i-1][-(i)]

o = abs(bc_sum - fr_sum)
print(o)



