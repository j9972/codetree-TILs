inp = list(input())

dic = {}

for i in inp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = 'None'
for k,v in dic.items():
    if v == 1:
        ans = k
        break
print(ans)