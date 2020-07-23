numbers = input().split()
target = input()
positions = [str(i) for i in range(len(numbers)) if numbers[i] == target]
print(" ".join(positions) or "not found")
