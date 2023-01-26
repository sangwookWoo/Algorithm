import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

list_ = []
for i in range(a, b + 1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt +=1
            if cnt > 1:
                break
    if cnt == 1:
        list_.append(i)
if len(list_) == 0:
    print(-1)
else :
    print(sum(list_), min(list_))