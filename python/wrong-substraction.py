def subtract_by_one(num, k):

    while(k):

        if num % 10 == 0:
            num = num // 10
       
        else:
            num = num - 1
         
        k -= 1
        
    return num


