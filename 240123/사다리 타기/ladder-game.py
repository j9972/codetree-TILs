n,m = map(int,input().split())

ans = list()
min_val = m

arr = list()
for i in range(m):
    a,b = map(int,input().split())
    arr.append((b,a-1))

arr.sort()

def possible():
    ppl1 = [i for i in range(n)]
    ppl2 = [i for i in range(n)]

    for _, idx in ans:
        ppl1[idx], ppl1[idx + 1] = ppl1[idx+ 1], ppl1[idx]
    for _, idx in arr:
        ppl2[idx], ppl2[idx + 1] = ppl2[idx+ 1], ppl2[idx]
    
    for i in range(n):
        if ppl1[i] != ppl2[i]:
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
    choose(cnt+1)


choose(0)
print(min_val)