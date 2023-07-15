def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : (x * 4)[:4], reverse = True)
    
    return str(int(''.join(numbers)))
    
    
    

    
# from itertools import permutations
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers = list(set(permutations(numbers, len(numbers))))
#     numbers = list(map(''.join, numbers))
#     numbers = list(map(int, numbers))
    
#     return str(max(numbers))
    