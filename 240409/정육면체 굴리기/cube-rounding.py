import copy

n,m,x,y,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

direction = list(map(int,input().split()))
dxs,dys = [0,0,-1,1],[1,-1,0,0] # 동서북남 순서

cube = [[0],
        [0, 0, 0, 0],
        [0]]

def move_cube(cube, d):
    new_cube = copy.deepcopy(cube)

    if d == 0: # RIGHT
        new_cube[0][0] = cube[1][0]
        new_cube[1][0] = cube[2][0]
        new_cube[1][2] = cube[0][0]
        new_cube[2][0] = cube[1][2]
    elif d == 1: # LEFT
        new_cube[0][0] = cube[1][2]
        new_cube[1][0] = cube[0][0]
        new_cube[1][2] = cube[2][0]
        new_cube[2][0] = cube[1][0]
    elif d == 2: # UP
        new_cube[0][0] = cube[1][1]
        new_cube[1][1] = cube[2][0]
        new_cube[1][3] = cube[0][0]
        new_cube[2][0] = cube[1][3]
    else: # DOWN
        new_cube[0][0] = cube[1][3]
        new_cube[1][1] = cube[0][0]
        new_cube[1][3] = cube[2][0]
        new_cube[2][0] = cube[1][1]

    return new_cube

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for d in direction:
    d -= 1

    nx,ny = x + dxs[d], y + dys[d]

    if not in_range(nx,ny):
        continue

    cube = move_cube(cube, d)

    if arr[nx][ny] == 0:
        arr[nx][ny] = cube[2][0]
    else:
        cube[2][0] =  arr[nx][ny]
        arr[nx][ny] = 0

    x,y = nx,ny

    print(cube[0][0])