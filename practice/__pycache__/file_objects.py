
with open('pattern1.py' , 'r') as f:
    size = 20
    f_contents = f.read(size)
    print(f_contents
    )
    f.seek(0)

    f_contents = f.read(size)
    print(f_contents)

    # f_contents = f.readline()

    # for line in f:
    #     print(line, end='')

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size)

    print(f.tell())
