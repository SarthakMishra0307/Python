from numpy import char


def countingValleys(steps, path):
    # Write your code here
    count = 0
    val_trav = 0
    char = []
    for i in range(steps):
        if 'D' in path[i]:
            count = count - 1
            char
        elif 'U' in path[i]:
            count = count + 1
            char[0] = 'U'
        if (char=='U' and count == 0):
            val_trav += 1
        # print(val_trav)
    return val_trav

steps = 8
path =  'UDDDUDUU'
countingValleys(steps, path)
