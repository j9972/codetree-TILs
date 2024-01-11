a,b = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

a_set = set()
b_set = set()

for i in a_list:
    if i not in b_list:
        a_set.add(i)
for i in b_list:
    if i not in a_list:
        b_set.add(i)

print(len(a_set) + len(b_set))