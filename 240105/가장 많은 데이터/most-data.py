n = int(input())

dic = {}
for _ in range(n):
    val = input()
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1

max_val = 0
for i in dic:
    max_val = max(max_val, dic[i])
print(max_val)