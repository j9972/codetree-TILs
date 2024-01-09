from collections import defaultdict
n,k = map(int,input().split())

arr = list(map(int,input().split()))

dic = defaultdict(int)

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
#print(dic)
sorted_dic = dict(sorted(dic.items(), key=lambda x: (-x[1], -x[0])))
#print(sorted_dic)

count = 0
for key in sorted_dic.keys():
    if count < k:
        print(key,end=' ')
        count += 1
    else:
        break