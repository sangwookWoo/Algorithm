from heapq import nlargest
def solution(citations):
    citations = sorted(citations, reverse = True)
    answer = []
    for h in range(1,1000):
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
            else :
                break
                
        if cnt <= h:
            return cnt

            
        
