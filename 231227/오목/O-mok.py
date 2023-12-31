import sys
arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

dxs = [-1,0,1,1]
dys = [1,1,1,0]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for x in range(19):
    for y in range(19):

        if arr[x][y] == 0:
            continue

        for i in range(4):
            dx, dy = dxs[i], dys[i]
            curx, cury = x, y
            val = arr[x][y]

            cnt = 1

            while True:
                nx ,ny = dx + curx , dy + cury

                if not in_range(nx,ny):
                    break
                if arr[nx][ny] != val:
                    break
                
                curx,cury = nx,ny
                cnt += 1
            
            if cnt == 5:
                print(val) 
                print((curx + x) // 2 + 1, (cury + y) // 2 + 1)
                sys.exit()
        
print(0)