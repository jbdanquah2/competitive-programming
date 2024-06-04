def execute_function(l, commands):
    x = 0
    stack = []
    
    for command in commands:
        if command == "add":
            x += 1
            if x >= 2**32:
                return "OVERFLOW!!!"
        elif command.startswith("for"):
            n = int(command.split()[1])
            stack.append(n)
        elif command == "end":
            if stack:
                n = stack.pop()
                if n > 1:
                    stack.append(n - 1)
                    stack.append(n - 1)
    
    return x

# Reading input
n = int(input())
commands = [input() for _ in range(n)]

# Executing the function and printing the result
result = execute_function(commands)
print(result)
