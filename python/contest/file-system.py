def get_lowest_num(new_name):
    
    num = 1
    
    while new_name + str(num) in name_request:
        num += 1
   
    return new_name + str(num)
        

n = int(input())

name_request = set()

for i in range(n):
    name = input().lower()
    
    if name not in name_request:
        name_request.add(name)
        print('OK')
    else:
        new_name = get_lowest_num(name)
        name_request.add(new_name)
        print(new_name)
    