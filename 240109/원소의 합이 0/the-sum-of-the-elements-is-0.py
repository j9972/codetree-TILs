from collections import defaultdict

n = int(input())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))
d_list = list(map(int,input().split()))

dic = {}

for i in range(n):
    for j in range(n):
        sum_val = a_list[i] + b_list[j]

        if sum_val in dic:
            dic[sum_val] += 1
        else:
            dic[sum_val] = 1

ans = 0
for i in range(n):
    for j in range(n):
        diff = -c_list[i] - d_list[j]

        if diff in dic:
            ans += dic[diff]
print(ans)