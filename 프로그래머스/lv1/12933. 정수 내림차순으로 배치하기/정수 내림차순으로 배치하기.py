def solution(n):
    a = str(n)
    answer = []
    for i in a:
        answer.append(i)
    
    answer.sort(reverse = True)
    return int(''.join(answer))