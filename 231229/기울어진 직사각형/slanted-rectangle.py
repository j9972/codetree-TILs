n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_value = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n



def getScore(x,y,i,j):
    move = [i,j,i,j]
    # 반시계 방향으로 4개의 대각선 방향
    dxs = [-1,-1,1,1]
    dys = [1,-1,-1,1]
    sum_val = 0

    for dx,dy,mv in zip(dxs,dys,move):
        for _ in range(mv):
            x ,y = x + dx, y + dy

            if not in_range(x,y):
                return 0
            
            sum_val += arr[x][y]
    return sum_val


for x in range(n):
    for y in range(n):
        for i in range(1,n):
            for j in range(1,n):
                max_value = max(max_value, getScore(x,y,i,j))
print(max_value)