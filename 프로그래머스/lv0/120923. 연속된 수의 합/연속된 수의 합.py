def solution(num, total):
    
    start = int(total / num) - int(num / 2) - 2
    
    
    while True:
        sum = 0
        for i in range(start, start + num):
            sum += i
        if sum == total:
            answer = list(range(start , start + num))
            break
        start += 1
        
    return answer