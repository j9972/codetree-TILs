n,k,p,t = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(t)
]

arr.sort(key = lambda x : x[0])

howManyShakeHands = [0] * (n+1)

infected = [False] * (n+1)
infected[p] = True

for i in arr:
    _, x, y = i

    if infected[x]:
        howManyShakeHands[x] += 1
    if infected[y]:
        howManyShakeHands[y] += 1

    if howManyShakeHands[x] <= k and infected[x]:
        infected[y] = True
    if howManyShakeHands[y] <= k and infected[y]:
        infected[x] = True

for i in range(1,n+1):
    if infected[i]:
        print(1, end='')
    else:
        print(0, end='')