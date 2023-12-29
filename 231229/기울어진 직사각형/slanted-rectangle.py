n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

ans = 0

def getScore(x,y,i,j):
    dxs,dys = [-1,-1,1,1],[1,-1,-1,1]
    move = [i,j,i,j]

    sum_val = 0

    for dx, dy, mv in zip(dxs,dys,move):
        for _ in range(mv):
            x = dx + x
            y = dy + y

            if not in_range(x,y):
                return 0
            
            sum_val += arr[x][y]
    return sum_val


for x in range(n):
    for y in range(n):
        for i in range(1,n):
            for j in range(1,n):
                ans = max(ans, getScore(x,y,i,j))
print(ans)