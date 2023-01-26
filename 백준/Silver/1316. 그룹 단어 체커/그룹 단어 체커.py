import sys
num = int(sys.stdin.readline())

cnt = 0
for _ in range(num):
    dic = {}
    word  = list(sys.stdin.readline().strip())
    for spe in word:
        dic.setdefault(spe, 0)
    for spe in word:
        dic[spe] += 1
    string = ''
    for k,v in dic.items():
        string += k * v
    if string == ''.join(word):
        cnt +=1
print(cnt)
        
        
            
        
            
    





