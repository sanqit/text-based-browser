with open("test.txt") as test_file:
    for line in test_file.readlines():
        print(line[0])
