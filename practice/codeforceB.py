t = int(input())
moves = ["U","D","L","R"]
candy =(1,1)
x_pos =0
y_pos =0
for i in range(t):
    curr_pos = (0,0)
    n_lenght = int(input())
    n = str(input())
    for j in n:
        if j == moves[0]:
            x_pos += 1
        elif j == moves[1]:
            x_pos -= 1
        elif j == moves[2]:
            y_pos -= 1
        elif j == moves[3]:
            y_pos += 1
        curr_pos = (x_pos,y_pos)
        # print(j, moves[0])
        # print(curr_pos)
        if curr_pos == candy:
            print("YES")
            break
    continue
    print("NO")

