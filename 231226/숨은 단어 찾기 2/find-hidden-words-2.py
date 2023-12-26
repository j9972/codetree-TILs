r, c = map(int, input().split())
arr = [
    list(input())
    for _ in range(r)
]

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

cnt = 0
for x in range(r):
    for y in range(c):
        if arr[x][y] != 'L':
            continue
        
        for i in range(8):
            dx, dy = dxs[i], dys[i]
            curx, cury = x, y
            val = 0

            while True:
                nx = curx + dx
                ny = cury + dy
                if not in_range(nx, ny):
                    break
                if arr[nx][ny] != 'E':
                    break

                val += 1
                curx, cury = nx, ny
            
            if val >= 2:
                cnt += 1
print(cnt)