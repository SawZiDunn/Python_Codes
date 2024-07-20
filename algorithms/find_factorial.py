def find_factorial_loop(n):
    
    if n < 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
        

def find_factorial_recursive(n):
    if n in [0, 1]:
        return 1

    return n * find_factorial_recursive(n - 1)

print(find_factorial_recursive(1))