from collections import Counter
def solution(nums):
    t = 0
    cnt = 0
    select = len(nums) / 2
    
    answer = Counter(nums)
    answer = list(dict(answer).values())
    answer.sort()
    
    for i in answer:
        if t < select:
            t += 1
            cnt += 1

    return cnt