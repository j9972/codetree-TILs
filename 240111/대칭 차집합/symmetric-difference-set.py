a,b = map(int,input().split())

a_list = set(map(int,input().split()))
b_list = set(map(int,input().split()))

ans = 0
for i in a_list:
    if i not in b_list:
        ans += 1
for i in b_list:
    if i not in a_list:
        ans += 1

print(ans)