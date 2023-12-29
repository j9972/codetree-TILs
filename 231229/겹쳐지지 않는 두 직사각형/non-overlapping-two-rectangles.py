n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 가능한 모든 rect 구하기
rect_list = list()
for i in range(n):
    for j in range(i,n):
        for k in range(m):
            for h in range(k,m):
                rect = [[0] * m for _ in range(n)]
                for r in range(i,j+1):
                    for c in range(k,h+1):
                        rect[r][c] = 1
                rect_list.append(rect)

# 충돌 체크
def inter(rect1, rect2):
    for r in range(n):
        for c in range(m):
            if rect1[r][c] and rect2[r][c]:
                return True
    return False

# 직사각형 합 구하기
def total(rect):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if rect[i][j]:
                cnt += arr[i][j]
    return cnt

ans = -1001
for i in range(len(rect_list)-1):
    for j in range(i+1,len(rect_list)):
        rect1 = rect_list[i]
        rect2 = rect_list[j]

        if inter(rect1,rect2):
            continue
        
        cnt = total(rect1) + total(rect2)
        ans = max(ans, cnt)

print(ans)