import sys
cnt = int(sys.stdin.readline())

for _ in range(cnt):
    num = int(sys.stdin.readline())
    dis = list(map(int, sys.stdin.readline().split()))
    dis.sort(reverse = True)
    list_1 = []
    list_2 = []
    for idx, i in enumerate(dis):
        if idx % 2 == 0:
            list_1.append(i)
        else:
            list_2.append(i)

    list_2.sort()
    list_1.extend(list_2)

    temp = 0
    for idx, i in enumerate(list_1):
        if idx != len(list_1) - 1:
            dif = abs(i - list_1[idx + 1])
            if temp < dif:
                temp = dif
        else:
            dif = abs(i - list_1[0])
            if temp < dif:
                temp = dif

    print(temp)



    

