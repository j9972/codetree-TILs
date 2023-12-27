arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

dxs = [-1,0,1,1]
dys = [1,1,1,0]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

ans = 0
flag = True
xx,yy=00,00

for x in range(19):
    for y in range(19):

        if arr[x][y] == 0:
            continue

        xx,yy=x,y

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
                ans = val 
                # print(curx, x)
                # print(cury, y)
                xx = (curx + x) // 2 + 1
                yy = (cury + y) // 2 + 1
                flag = False
                break
        
        if not flag:
            break
    if not flag:
        break

if ans != 0:
    print(ans)
    print(xx,yy)
else:
    print(0)