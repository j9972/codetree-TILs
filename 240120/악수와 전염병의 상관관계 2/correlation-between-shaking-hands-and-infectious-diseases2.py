n,k,p,t = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(t)
]

arr.sort(key = lambda x : x[0]) # 악수한 시간에 맞춰 정렬

d = [0] * (n+1)
infect = [False] * (n+1)
infect[p] = True
            
for i in arr:
    _,x,y = i

    if infect[x]:
        d[x] += 1
    if infect[y]:
        d[y] += 1
    
    if d[x] <= k and infect[x]:
        infect[y] = True
    if d[y] <= k and infect[y]:
        infect[x] = True

for i in range(1,n+1):
    if infect[i] == True:
        print(1,end='')
    else:
        print(0,end='')