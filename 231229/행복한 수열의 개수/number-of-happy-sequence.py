n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0

def cnt_chect(cnt):
    return cnt == m

def happy(new):
    cnt = 1
    for a in range(n-m+1): # 2번

        for j in range(a,a+m-1): # 0

            if new[j] != new[j+1]:
                
                if cnt_chect(cnt):
                    return True
                break

            cnt += 1
        
        if cnt_chect(cnt):
            return True

    return False

# 가로
for i in range(n):
    new = arr[i][:]
    if happy(new):
        ans += 1

# 세로
for i in range(n):
    new = list()
    for j in range(n):
        new.append(arr[j][i])
    if happy(new):
        ans += 1
print(ans)