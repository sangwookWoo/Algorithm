import sys
num = int(sys.stdin.readline())

list_ = []
for _ in range(num):
    list_.append(tuple(map(int,sys.stdin.readline().split())))
    
list_.sort(key = lambda x : [x[0], x[1]])

total = 0
for i in list_:
    if total < i[0]:
        total = sum(i)
    else:
        total += i[1]
print(total)
        