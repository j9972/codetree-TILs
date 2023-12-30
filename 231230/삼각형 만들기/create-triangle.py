n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
# 삼각형 넓이 구하는 신발끈 공식
def getArea(x1,y1, x2,y2, x3,y3):
    return abs((x1 * y2 + x2 * y3 + x3 * y1) -
               (x2 * y1 + x3 * y2 + x1 * y3))
ans = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1,y1 = segments[i]
            x2,y2 = segments[j]
            x3,y3 = segments[k]

            if (x1==x2 or x2==x3 or x3==x1) and (y1==y2 or y2==y3 or y1==y3):
                ans = max(ans, getArea(x1,y1, x2,y2, x3,y3))

print(ans)