n,m = map(int,input().split())

arr = [
    list(input())
    for _ in range(n)
]

red_pos, blue_pos = (0,0), (0,0)
OUT_MAP = (n,m)
ans = 11

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            arr[i][j] = 0
            red_pos = (i,j)
        elif arr[i][j] == 'B':
            arr[i][j] = 0
            blue_pos = (i,j)
        elif arr[i][j] == '#': # 벽
            arr[i][j] = 1
        elif arr[i][j] == '.':
            arr[i][j] = 0
        elif arr[i][j] == 'O': # 출구
            arr[i][j] = 2

def red_exit():
    return red_pos != OUT_MAP

def blue_exit():
    return blue_pos != OUT_MAP

def can_go(x,y):
    return arr[x][y] != 1 and (x,y) != red_pos and (x,y) != blue_pos

def red_first(direct):
    (rx,ry), (bx,by) = red_pos, blue_pos

    if direct == 0:
        return (ry == by) and (rx < bx)
    elif direct == 1:
        return (ry == by) and (rx > bx)
    elif direct == 2:
        return (rx == bx) and (ry < by)
    elif direct == 3:
        return (rx == bx) and (ry > by)

def get_dest(pos, direct):
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    x,y = pos

    nx,ny = x + dx[direct] , y + dy[direct]

    if not can_go(nx,ny):
        return pos
    if arr[nx][ny] == 2:
        return OUT_MAP
    return get_dest((nx,ny), direct)


def move(direct):
    global red_pos, blue_pos

    if red_first(direct):
        red_pos = get_dest(red_pos, direct)
        blue_pos = get_dest(blue_pos, direct)
    else:
        blue_pos = get_dest(blue_pos, direct)
        red_pos = get_dest(red_pos, direct)

def choose(cnt):
    global ans, red_pos, blue_pos

    if not blue_exit():
        return

    if not red_exit():
        ans = min(ans, cnt)
        return

    if cnt >= 10:
        return 

    for d in range(4):
        tmp_red, tmp_blue = red_pos, blue_pos

        move(d)
        choose(cnt + 1)

        red_pos, blue_pos = tmp_red, tmp_blue 

choose(0)
if ans >= 11:
    ans = -1

print(ans)