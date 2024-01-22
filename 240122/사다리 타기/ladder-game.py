n,m = map(int,input().split())

arr = []
for i in range(m):
    a,b = tuple(map(int,input().split()))
    arr.append((b, a-1))

arr.sort()

min_val = m
ans = []

def possible():
    pp1 = [i for i in range(n)]
    pp2 = [i for i in range(n)]

    for _ , idx in arr:
        pp1[idx], pp1[idx+1] = pp1[idx+1], pp1[idx]
    for _ , idx in ans:
        pp2[idx], pp2[idx+1] = pp2[idx+1], pp2[idx]
    
    for i in range(n):
        if pp1[i] != pp2[i]:
            return False
    
    return True

def choose(cnt):
    global min_val

    if cnt == m:
        if possible():
            min_val = min(min_val, len(ans))
        return
    
    ans.append(arr[cnt])
    choose(cnt+1)
    ans.pop()
    choose(cnt+1) # 선택안된 줄에 대해서 실행을 한번더

choose(0)
print(min_val)