n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def nega(a,b,c,d):
    for i in range(a,b+1):
        for j in range(c,d+1):
            if arr[i][j] <= 0:
                return False
    return True

# 가능한 모든 rect 구하기
rect_list = list()
for i in range(n):
    for j in range(i,n):
        for k in range(m):
            for h in range(k,m):
                if nega(i,j,k,h):
                    rect = [[0] * m for _ in range(n)]
                    for r in range(i,j+1):
                        for c in range(k,h+1):
                            rect[r][c] = 1
                    rect_list.append(rect)

# 직사각형 합 구하기
def total(rect):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if rect[i][j]:
                cnt += 1
    return cnt

ans = -1001
for i in rect_list:
    ans = max(ans, total(i))

if ans == -1001:
    print(-1)
else:
    print(ans)