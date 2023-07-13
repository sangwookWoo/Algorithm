def solution(s):
    answer = []
    dict_ = {}
    for idx, apb in enumerate(s):
        
        if apb in dict_.keys():
            result = idx - dict_[apb]
            answer.append(result)
            dict_[apb] = idx
            
        else :
            dict_[apb] = idx
            answer.append(-1) 
    return answer