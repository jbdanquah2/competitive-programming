entry = input().spli(" ")
num = entry[0]
k = entry[1]

while(k):

    if num % 10 == 0:
        num = num // 10

    else:
        num = num - 1

    k -= 1

return num


