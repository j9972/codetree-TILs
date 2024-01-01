d,h,m = map(int,input().split())

diff = (d * 24 * 60 + h * 60 + m) - (11 * 24 * 60 + 11 * 60 + 11)

# 출력
if diff < 0:
    print(-1)
else:
    print(diff)