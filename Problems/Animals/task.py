with open("animals.txt") as animals_file:
    with open("animals_new.txt", "w") as animals_new_file:
        animals_new_file.write(" ".join(animals_file.read().split()))
