def solution(brown, yellow):
    answer = []

    
    for n in range(3, 3000):
        for m in range(3, 3000):
            if (yellow == (m - 2) * (n - 2)) and (brown ==  2 * m + 2 * n - 4):
                return [m,n]
    