n, m, score, k = 6, 4, 0, int(input())

arr = [
    [
        [0 for _ in range(4)]
        for _ in range(6)
    ]
    for _ in range(2)
]

shape = [
    [],

    [
        [1,0],
        [0,0]
    ],

    [
        [1,1],
        [0,0]
    ],

    [
        [1,0],
        [1,0]
    ]
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(t,x,y,color):
    for dx in range(2):
        for dy in range(2):
            if shape[t][dx][dy]:
                nx,ny = x + dx, y + dy

                if not in_range(nx,ny) or arr[color][nx][ny]:
                    return False
    return True

def put(color, t,x,y):
    for dx in range(2):
        for dy in range(2):
            if shape[t][dx][dy]:
                nx,ny = x + dx, y + dy
                arr[color][nx][ny] = 1

def full_line(color, row):
    return all([
        arr[color][row][col] == 1
        for col in range(m)
    ])

def drop_one_line(color, end_row):
    for i in range(end_row,0,-1):
        for j in range(m):
            arr[color][i][j] = arr[color][i-1][j]
            arr[color][i-1][j] = 0

def exist_block(color, row):
    return any([
        arr[color][row][col] == 1
        for col in range(m)
    ])

def dark(color):
    global score

    row = n-1
    while (row>=2):
        if full_line(color, row):
            score += 1
            drop_one_line(color, row)
        else:
            row -= 1

def light(color):
    cnt = 0
    for i in range(2):
        if exist_block(color, i):
            cnt += 1
    
    for _ in range(cnt):
        drop_one_line(color, n-1)

def drop(color, t, col):
    for row in range(n):
        if not can_go(t, row + 1, col, color):
            put(color, t, row, col)
            break
    
    dark(color)
    light(color)

def simulate(t,x,y):
    drop(0,t,y)

    if t == 1:
        drop(1,1,m-1-x)
    elif t == 2:
        drop(1,3,m-1-x)
    elif t == 3:
        drop(1,2,m-1-(x+1))

def remain():
    return sum([
        arr[l][i][j]
        for l in range(2)
        for i in range(n)
        for j in range(m)
    ])

for _ in range(k):
    t,x,y = map(int,input().split())
    simulate(t,x,y)

print(score)
print(remain())