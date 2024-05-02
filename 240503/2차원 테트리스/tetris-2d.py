n,m,k = 6,4,int(input())

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

arr =[
    [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    for _ in range(2)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

score = 0

def can_go(num, t, x, y):
    for dx in range(2):
        for dy in range(2):
            if shape[t][dx][dy]:
                nx,ny = x + dx, y + dy

                if not in_range(nx,ny) or arr[num][nx][ny]:
                    return False
    return True

def put(num, t, x, y):
    for dx in range(2):
        for dy in range(2):
            if shape[t][dx][dy]:
                nx,ny = x + dx, y + dy

                arr[num][nx][ny] = 1

def remain():
    return sum([
        arr[l][i][j]
        for l in range(2)
        for i in range(n)
        for j in range(m)
    ])

def full_line(num, row):
    return all([
        arr[num][row][col] == 1
        for col in range(m)
    ])


def is_exist(num, row):
    return any([
        arr[num][row][col] == 1
        for col in range(m)
    ])

def drop_one(num, end_row):
    for i in range(end_row, 0,-1):
        for j in range(m):
            arr[num][i][j] = arr[num][i-1][j]
            arr[num][i-1][j] = 0

def dark(num):
    global score 

    for i in range(n-1, 1,-1):
        if full_line(num, i):
            score += 1
            drop_one(num, i)

def light(num):
    cnt = 0
    for i in range(2):
        if is_exist(num, i):
            cnt += 1
    
    for i in range(cnt):
        drop_one(num, n-1)

def drop(num, t, y):
    for x in range(n):
        if not can_go(num, t, x+1, y):
            put(num, t, x, y)
            break
    
    dark(num)
    light(num)

def simulate(t, x, y):
    drop(0, t, y)

    if t == 1:
        drop(1,1,m-1-x)
    elif t == 2:
        drop(1,3,m-1-x)
    else:
        drop(1,2,m-1-(x+1))

for i in range(k):
    t,x,y = map(int,input().split())
    simulate(t,x,y)

print(score)
print(remain())