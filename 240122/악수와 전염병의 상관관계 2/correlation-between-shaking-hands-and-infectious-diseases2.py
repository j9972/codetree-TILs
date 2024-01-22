n,k,p,t = map(int,input().split())

infected = [False] * (n+1)
infected[p] = True
shake = [0] * n

arr = [
    list(map(int,input().split()))
    for _ in range(t)
]

for i in arr:
    _, x,y = i

    if infected[x]:
        shake[x] += 1
    if infected[y]:
        shake[y] += 1

    if infected[x] and shake[x] <= k:
        infected[y] = True
    if infected[y] and shake[y] <= k:
        infected[x] = True
    
for i in range(n):
    if infected[i]:
        print(1,end='')
    else:
        print(0,end='')