from collections import deque

n = int(input())

commands = deque(input() for _ in range(n))
stack = deque()
while commands:
    cmd = commands.popleft().split()
    op = cmd[0]
    if op == "PUSH":
        val = cmd[1]
        stack.append(val)
    elif op == "POP":
        stack.pop()

while stack:
    print(stack.pop())
