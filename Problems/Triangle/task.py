height = int(input())
h = -1
for _ in range(height):
    h += 2
    print(("#" * h).center(height * 2 - 1))
