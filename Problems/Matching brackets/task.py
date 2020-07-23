brackets = 0
for symbol in input():
    if symbol == "(":
        brackets += 1
    elif symbol == ")":
        brackets -= 1
    if brackets < 0:
        break

print("OK" if brackets == 0 else "ERROR")
