
def main(nums, m):

    sorted_nums = sorted(nums, reverse=True)
    stack = []
    count_zeroes = 0
    smallest = ''

    for num in sorted_nums:
        if num != 0:
            stack.append(num)
        else:
            count_zeroes += 1

    if len(stack) > 0:
        smallest = str(stack.pop()) + '0' * count_zeroes


    for _ in range(len(stack)):
        smallest += str(stack.pop())
    
    if len(smallest) < 1:
       return 'WRONG_ANSWER' 

    return 'OK' if int(smallest) == m else 'WRONG_ANSWER'
            
        
n = list(map(int, input()))
m = int(input())
print(main(n, m))