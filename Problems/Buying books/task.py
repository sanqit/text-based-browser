n = int(input())

book_shelf = []
readed = []

for _ in range(n):
    cmd = input().split(" ", 1)
    if cmd[0] == "BUY":
        book_shelf.append(cmd[1])
    elif cmd[0] == "READ":
        readed.append(book_shelf.pop())

while readed:
    print(readed.pop())
