n,g = map(int,input().split())

s = set({1})

for _ in range(g):
    arr = list(map(int,input().split()))

    tmp = set()
    cnt = 0
    for i in range(1,arr[0]+1):
        if arr[i] in s:
            cnt += 1
        else:
            tmp.add(arr[i])

    #print("tmp : ", tmp)
    if cnt == arr[0]-1:
        for i in tmp:
            s.add(i)

print(len(s))