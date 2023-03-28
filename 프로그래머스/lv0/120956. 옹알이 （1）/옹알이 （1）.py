from itertools import permutations

def pmts(iterator):
    words = [] 
    for iter in range(1,5):
        for i in permutations(iterator, iter):
            words.append(''.join(list(i)))
    return words
    
def solution(babbling):
    canprn = pmts(["aya", "ye", "woo", "ma"])
    
    count = 0 
    for word in babbling:
        if word in canprn:
            count += 1
    return count
            
