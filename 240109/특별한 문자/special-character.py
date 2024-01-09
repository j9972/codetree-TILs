import sys
inp = list(input())

dic = {}

for i in inp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


for k,v in dic.items():
    if v == 1:
        print(k)
        sys.exit()
print("None")