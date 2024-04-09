from collections import deque
import copy

n,m,x,y,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

direction = list(map(int,input().split()))
dxs,dys = [0,0,-1,1],[1,-1,0,0] # 동서북남 순서

dice = [0 for _ in range(7)]

up, front, right = 1,2,3

def in_range(x,y):
    return 0<=x<n and 0<=y<m

q = deque()
q.append((x,y))

for d in direction:
    d -= 1

    x,y = q.popleft()

    nx,ny = x + dxs[d], y + dys[d]

    if not in_range(nx,ny):
        q.append((x,y))
        continue

    if d == 0:
        up, front, right = 7-right,front, up
    elif d == 1:
        up, front, right = right,front, 7-up
    elif d == 2:
        up, front, right = front, 7-up, right
    elif d == 3:
        up, front, right = 7 - front, up, right
    
    bottom = 7 - up

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[bottom]
    else:
        dice[bottom] = arr[nx][ny]
        arr[nx][ny] = 0

    q.append((nx,ny))

    print(dice[up])