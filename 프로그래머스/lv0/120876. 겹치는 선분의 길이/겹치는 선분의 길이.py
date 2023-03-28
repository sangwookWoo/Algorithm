
def solution(lines):
    arr = []
    for i in lines:
        arr.append(i[0])
        arr.append(i[1])
    
    start = min(arr)
    end = max(arr)
    
    vin_dict = {}
    while start <= end:
        vin_dict[start] = 0
        start += 1
    
    for j in range(3):
        for i in range(lines[j][0],lines[j][1]):
            vin_dict[i] += 1
        
    sum = 0
    for i in vin_dict:
        if vin_dict[i] >= 2:
            sum += 1
            
    return sum
        
        