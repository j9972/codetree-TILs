n,k,p,T = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(T)
]

arr.sort(key = lambda x:x[0])

d = [0] * (n+1)
infect = [False] * (n+1)
infect[p] = True

for i in arr:
    _, x, y = i
    
    if infect[x]:
        d[x] += 1
    if infect[y]:
        d[y] += 1

    if d[x] <= k and infect[x]:
        infect[y] = True
    if d[y] <= k and infect[y]:
        infect[x] = True

for i in infect[1:]:
    if i == True:
        print(1,end="")
    else:
        print(0,end="")