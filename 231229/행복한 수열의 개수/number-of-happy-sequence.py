n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0

def happy(new):
    cnt = 1
    
    for i in range(n-m+1): # 2번
        f = False
        for j in range(i,i+m-1): # 0
            
            if new[j] != new[j+1]:  
                f = True  
                break
                
            cnt += 1
        
        if cnt == m:
            return True
        if f:
            break
    return False

# 가로
for i in range(n):
    new = arr[i][:]
    if happy(new):
        print(new)
        ans += 1

# 세로
for i in range(n):
    new = list()
    for j in range(n):
        new.append(arr[j][i])
    if happy(new):
        ans += 1
print(ans)