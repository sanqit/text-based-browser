with open("salary.txt") as salary_file, open("salary_year.txt", "w") as salary_year_file:
    for line in salary_file.readlines():
        salary_year_file.write(f"{str(int(line) * 12)}\n")
