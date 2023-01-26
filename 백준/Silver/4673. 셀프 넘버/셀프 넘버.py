def self_number(x):
    return x + sum(list(map(int,list(str(x)))))

num = 10000
list_ = [self_number(x) for x in range(1, num) if self_number(x) < num]
for i in range(1, num):
    if i not in set(list_):
        print(i)