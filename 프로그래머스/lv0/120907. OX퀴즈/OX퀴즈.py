def solution(quiz):
    list_ = []
    for i in quiz:
        problem = i.split(' ')
        
        x = int(problem[0])
        y = int(problem[2])
        
        if problem[1] == "-":
            if x - y == int(problem[4]):
                list_.append("O")
            else :
                list_.append("X")
                
        if problem[1] == "+":
            if x + y == int(problem[4]):
                list_.append("O")
            else :
                list_.append("X")
                
    return list_
        
        
                
                