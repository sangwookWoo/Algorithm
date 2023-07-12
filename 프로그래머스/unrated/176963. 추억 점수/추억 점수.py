def solution(name, yearning, photo):
    answer = []
    
    # name, yearning 합산한 dict 생성
    dict_ = {}
    for n, y in zip(name, yearning):
        dict_[n] = y
    
    for p in photo:
        score = 0
        for nm in p:
            if nm in dict_.keys():
                score += dict_[nm]
        answer.append(score)
            
            
    
    return answer