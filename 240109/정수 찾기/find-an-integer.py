a = int(input())
a_list = list(map(int,input().split()))

b = int(input())
b_set = set(list(map(int,input().split())))

for val_b in b_set:
    if val_b in a_list:
        print(1)
    else:
        print(0)