# Problem: C - Radio Station - https://codeforces.com/gym/500425/problem/C

nm = input()

n, m = [int(num) for num in nm.split()]

servers = {}

for i in range(n):
    name, ip = input().split()
    servers[ip+';'] = name

for i in range(m):
    cmd = input()
    ip = cmd.split()[1]
    
    print(f"{cmd} #{servers[ip]}")
