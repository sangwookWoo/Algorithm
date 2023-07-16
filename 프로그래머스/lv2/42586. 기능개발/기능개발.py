def solution(progresses, speeds):
    answer = []
    
    while True:
        
        
        cnt = 0
        while True:
            
            if len(progresses) != 0:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    if cnt > 0:
                        answer.append(cnt)
                    break
            else:
                if cnt > 0:
                    answer.append(cnt)
                break
        
        if len(progresses) != 0:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        else :
            break

    
    return answer