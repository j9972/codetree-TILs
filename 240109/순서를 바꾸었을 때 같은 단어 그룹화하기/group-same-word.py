from collections import defaultdict

n = int(input())
# res = []

# for _ in range(n):
#     val = input()

#     dic = defaultdict(int)

#     for i in val:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#     res.append(dic)

# max_val = 0
# for i in range(len(res)):
#     val = 1
#     for j in range(i+1,len(res)):
#         if res[i] == res[j]:
#             val += 1
#     max_val = max(max_val, val)
# print(max_val)

dic = {}

for _ in range(n):
    val = input()
    val_sorted = sorted(val)

    string = ""
    for e in val_sorted:
        string += e
    
    if string in dic:
        dic[string] += 1
    else:
        dic[string] = 1

res = 0
for k,v in dic.items():
    if res < v:
        res = v
print(res)