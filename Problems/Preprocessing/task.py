text = input()
for char in ",.!?":
    text = text.replace(char, "")
print(text.lower())
