def startswith_capital_counter(names):
    return sum(name.istitle() for name in names)
