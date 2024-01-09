a = int(input())
a_list = set(list(map(int,input().split())))
b = int(input())
b_set = list(map(int,input().split()))

for val_b in b_set:
    if val_b not in a_list:
        print(0)
    else:
        print(1)