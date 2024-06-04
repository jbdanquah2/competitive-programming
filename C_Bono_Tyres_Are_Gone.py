n = int(input())
commands = []
for _ in range(2 * n):
    commands.append(input().split())

print(commands)

stack = []
reorders = 0

for cmd in commands:
    if cmd[0] == "add":
        stack.append(cmd[1])
    else:  
        if stack: 
            if stack[-1]: 
                stack.pop()
            else:
                reorders += 1
                stack = [] 

print(reorders - 1)
