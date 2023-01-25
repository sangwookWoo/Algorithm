import sys
dorara = int(sys.stdin.readline())
for _ in range(dorara):
    num = int(sys.stdin.readline())
    list_ = []

    for _ in range(num):
        list_.append(tuple(map(int,sys.stdin.readline().split())))
    list_.sort(key = lambda x : [x[0], x[1]])

    cnt = 0
    smallest = num
    for s, m in list_:
        if m <= smallest:
            smallest = m
            cnt += 1
            
    print(cnt)





    

