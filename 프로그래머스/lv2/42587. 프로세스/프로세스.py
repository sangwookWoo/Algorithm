# priorities를 순회한다.
# 프로세스 실행 시도
# 시도하다, 우선순위가 큰게 리스트 안에 있으면 리스트의 맨 뒤로 집어넣는다(pop 한뒤 append)
# 맨 뒤로 집어넣은 것이 temp_idx일 경우 temp_idx를 해당 priorities의 길이 - 1로 변경
# 프로세스 실행시에는 얘를 pop으로 빼냄

def solution(priorities, location):
    cnt = 0
    
    # 반복하고
    while len(priorities) != 0:
        
        if max(priorities) > priorities[0]:
            priorities.append(priorities.pop(0))
            location = (location - 1 + len(priorities)) % len(priorities)

        else :
            cnt += 1
            if location == 0:
                return cnt
            else :
                priorities.pop(0)
                location = (location - 1 + len(priorities)) % len(priorities)
