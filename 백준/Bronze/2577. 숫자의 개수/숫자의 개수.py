import sys


list_ = []
for _ in range(3):
    list_.append(int(sys.stdin.readline()))

a, b, c = list_
new_list = list(str(a * b * c))
# print(list(str(a * b * c)))
dic = {}
for i in new_list:
    dic[i] = 0
for i in new_list:
    dic[i] += 1

for i in range(10):
    try:
        print(dic[str(i)])
    except :
        print(0)
    
    
        
    
    






