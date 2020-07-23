with open("sums.txt") as sums_file:
    for line in sums_file.readlines():
        print(sum(map(int, line.split())))
