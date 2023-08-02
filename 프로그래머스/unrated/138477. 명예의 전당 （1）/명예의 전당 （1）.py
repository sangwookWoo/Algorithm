def solution(k, score):
    answer = []
    real_answer = []
    for i in score:
        if len(answer) < k:
            answer.append(i)
        else:
            answer.append(i)
            answer.sort(reverse = True)
            answer = answer[:k]
        
        real_answer.append(min(answer))
        
    
    return real_answer