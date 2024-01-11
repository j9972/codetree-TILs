n,g = map(int,input().split())

arr =[
    list(map(int,input().split()))
    for _ in range(g)
]

arr.sort(key=lambda x:x[0])

s = set({1})

for i in range(g):
    new_arr = arr[i]

    tmp = set()
    
    for j in range(1,new_arr[0]+1):
        if new_arr[j] not in s:
            tmp.add(new_arr[j])

    if len(tmp) == 1:
        for j in tmp:
            s.add(j)

print(len(s))