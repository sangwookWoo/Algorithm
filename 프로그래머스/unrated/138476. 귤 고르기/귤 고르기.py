from collections import Counter

def solution(k, tangerine):
    total = 0
    answer = 0
    for i, v in Counter(tangerine).most_common(k):
        total += v
        answer += 1
        if total >= k:
            return answer
