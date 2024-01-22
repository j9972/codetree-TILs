import sys

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = -sys.maxsize
ans = []

boomCnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            boomCnt += 1

block1 = [(-2,0),(-1,0),(1,0),(2,0)]
block2 = [(0,-1),(-1,0),(1,0),(0,1)]
block3 = [(-1,-1),(-1,1),(1,1),(1,-1)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def boom():
    tmp = [[0] * n for _ in range(n)]
    
    for i in ans:
        val, x, y = i

        tmp[x][y] = 1

        if val == 1:
            for j in block1:
                next_x, next_y = j

                if not in_range(x + next_x, y + next_y):
                    continue

                tmp[x + next_x][y + next_y] = 1

        elif val == 2:
            for j in block2:
                next_x, next_y = j

                if not in_range(x + next_x, y + next_y):
                    continue

                tmp[x + next_x][y + next_y] = 1

        elif val == 3:
            for j in block3:
                next_x, next_y = j

                if not in_range(x + next_x, y + next_y):
                    continue

                tmp[x + next_x][y + next_y] = 1
    
    size = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 1:
                size += 1
    return size


def choose(cnt):
    global max_val

    if cnt == boomCnt:
        max_val = max(max_val, boom())
        return

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                for i in range(1,4):
                    ans.append((i, x, y))
                    choose(cnt+1)
                    ans.pop()


choose(0)
print(max_val)