n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

boom_list = list()
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            boom_list.append((i,j))

max_val = 0
def Print():
    global max_val
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                cnt += 1
    if max_val < cnt:
        max_val = cnt
    
def handle(idx, i , boolean):
    x,y = boom_list[idx][0], boom_list[idx][1]

    if i == 1: # 위 아래 두개 초토화
        dirs = ((1,0),(-1,0),(2,0),(-2,0))
    elif i == 2: # 십자 모양 초토화
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
    else:       # 대각선 모양 초토화
        dirs = ((-1,-1),(1,-1),(1,1),(-1,1))
    
    if boolean:
        factor = 1
    else:
        factor = -1
    
    for d in range(4):
        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if not in_range(nx,ny):
            continue
        arr[nx][ny] += factor

def choose(cur):
    if cur == len(boom_list):
        Print()
        return 

    for i in range(1,4):
        handle(cur, i, True)
        choose(cur + 1)
        handle(cur, i, False)

choose(0)
print(max_val)