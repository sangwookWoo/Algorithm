# people 리스트 정렬(오름차순)
# 가장 가벼운 사람과 가장 무거운 사람이 limit이 초과하지 않는다면 answer +=1
# 그런데 가장 무거운 사람만 탑승할 수 있다면 그냥 무거운 사람만 두고 answer += 1

from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while len(people) >= 2:
        
        if people[0] + people[-1] > limit:
            people.pop()
            answer += 1

        else :
            answer += 1
            people.popleft()
            people.pop()
            
        if len(people) == 1:
            answer += 1
            break
            
        # print(people)
            

    
    return answer
        