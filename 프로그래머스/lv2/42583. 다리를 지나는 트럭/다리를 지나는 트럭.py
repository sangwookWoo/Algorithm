# deque로 구현
# queue를 bridge_length만큼 만든 뒤
# queue의 총합이 weight보다 낮을 경우
# truck_weights를 하나씩 다리 위로 올린다(queue에 올린다)
    # 올라갔을 때는 항상 하나씩 작아지면서 맨 뒤에껄 0으로 업데이트해야함
    # popleft를 하고, 뒤에 append로 쌓아야함
    # 하지만 popleft할 때 append는 항상 0으로만 하면됨
# 마지막에 sum 했을 때 0이면 종료

from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    queue = [0] * bridge_length
    queue = deque(queue)
    
    on_weights = 0 
    while len(queue) != 0:
        if len(truck_weights) != 0:
            
            # queue에 맨 앞에 값이 들어오면 빼줘야한다.
            # 곧 나갈 것이기 때문에 다리 위에 올릴 수 있음
            
            if on_weights + truck_weights[0] - queue[0] <= weight:
                on_weights += truck_weights[0]
                on_weights -= queue[0]
                queue.popleft()
                queue.append(truck_weights.pop(0))
                cnt += 1
                
            else :
                on_weights -= queue[0]
                queue.popleft()
                queue.append(0)
                cnt += 1
                
        else :
            on_weights -= queue[0]
            queue.popleft()
            cnt += 1
            
    return cnt
        
        
        