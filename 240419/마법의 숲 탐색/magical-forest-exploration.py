from collections import deque
r,c,k = map(int,input().split())

# 북 동 남 서
dxs,dys = [-1,0,1,0],[0,1,0,-1]

MAX_L = 70

arr = [
    [0 for _ in range(MAX_L)]
    for _ in range(MAX_L+3)
]

is_exit = [
    [False] * MAX_L
    for _ in range(MAX_L+3)
]

ans = 0

# 벗어나면 북쪽으로 넘어간다는 의미로 볼 수도 있다., 중앙 위치가 가장 남쪽보다 한칸 위여야 함
def in_range(x,y):
    return 3<=x<r+3 and 0<=y<c

sur_x, sur_y = [-1,-1,-1,0,0,0,1], [-1,0,1,-1,0,1,0]
def can_go(x,y):
    flag = 0 <= y - 1 and y + 1 < c and x + 1 < r + 3
    for sx, sy in zip(sur_x, sur_y):
        nx,ny = x + sx, y + sy
        flag = flag and arr[nx][ny] == 0
    
    return flag

# def can_go(x,y):
#     flag = 0 <= y - 1 and y + 1 < c and x + 1 < r + 3
#     flag = flag and (arr[x - 1][y - 1] == 0)
#     flag = flag and (arr[x - 1][y] == 0)
#     flag = flag and (arr[x - 1][y + 1] == 0)
#     flag = flag and (arr[x][y - 1] == 0)
#     flag = flag and (arr[x][y] == 0)
#     flag = flag and (arr[x][y + 1] == 0)
#     flag = flag and (arr[x + 1][y] == 0)
#     return flag

def reset():
    for i in range(r+3):
        for j in range(c):
            arr[i][j] = 0
            is_exit[i][j] = False

def bfs(x,y):
    res = x

    q = deque([(x,y)])

    visit = [
        [False] * c
        for _ in range(r+3)
    ]
    visit[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx,ny = cur_x + dx, cur_y + dy

            if in_range(nx,ny) and not visit[nx][ny] and (arr[nx][ny] == arr[cur_x][cur_y] or (arr[nx][ny] != 0 and is_exit[cur_x][cur_y])):
                q.append((nx,ny))
                visit[nx][ny] = True
                res = max(res, nx)
    return res

def move(x,y,d,num):
    global ans
    if can_go(x+1,y):
        move(x+1,y,d,num)

    elif can_go(x+1,y-1):
        move(x+1, y-1, (d+3)%4, num)

    elif can_go(x+1,y+1):
        move(x+1, y+1, (d+1)%4, num)

    else:
        if not in_range(x-1, y-1) or not in_range(x+1,y+1):
            reset()

        else:
            arr[x][y] = num
            for dx, dy in zip(dxs,dys):
                arr[x + dx][y + dy] = num
            
            is_exit[x + dxs[d]][y + dys[d]] = True
            ans += bfs(x,y) - 3 + 1

for num in range(1,k+1):
    y,d = map(int,input().split())
    move(0,y-1,d,num)

print(ans)