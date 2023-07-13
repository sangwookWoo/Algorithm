from itertools import permutations

def solution(babbling):
    answer = []
    
    pronun = ["aya", "ye", "woo", "ma"]
    for i in range(1, len(pronun) + 1):
        res = list(permutations(pronun, i))
        for x in res:
            abc = ''.join(x)
            answer.append(abc)
    
    cnt = 0
    for i in babbling:
        if i in answer:
            cnt += 1
    
    return cnt