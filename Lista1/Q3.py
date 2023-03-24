def sum_to(n):
    if n == 1:
        return 1
    return n + sum_to(n-1)

S = sum_to(10)
print(S)


    
        
        
