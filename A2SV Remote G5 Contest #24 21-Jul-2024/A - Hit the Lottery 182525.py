# Problem: A - Hit the Lottery - https://codeforces.com/gym/536373/problem/A



def main(amount: int): 
    moves = 0
    
    while amount > 0:
          
        if amount >= 100: 
            amount -= 100
            moves += 1    

        elif amount >= 20: 
            amount -= 20
            moves += 1
        elif amount >= 10: 
            amount -= 10
            moves += 1
        elif amount >= 5: 
            amount -= 5
            moves += 1
        else: 
            amount -= 1
            moves += 1
            
    return moves
    
amount = int(input())
print(main(amount))
