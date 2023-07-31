from collections import deque

def solution(food):
    
    answer = deque([0])
    
    food = food[::-1]
    print(food[:-1])
    for idx, i in enumerate(food[:-1]):
        # 짝수로 배치
        i = i - i % 2
        
        idx = len(food) - idx - 1
        for _ in range(i):
            if _ % 2 == 0:
                answer.appendleft(idx)

            else:
                answer.append(idx)
    
    st = ''
    for i in list(answer):
        st += str(i)
        
    return st