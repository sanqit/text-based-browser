numbers = [int(x) for x in input()]
print([sum(numbers[:x + 1]) for x in range(len(numbers))])
