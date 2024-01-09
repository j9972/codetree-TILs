n = int(input())

dic = {}
for i in range(n):
    x,y = map(int,input().split())

    if x in dic:
        if dic[x] > y:
            dic[x] = y
    else:
        dic[x] = y

sum_val = 0
for k,v in dic.items():
    sum_val += v
print(sum_val)