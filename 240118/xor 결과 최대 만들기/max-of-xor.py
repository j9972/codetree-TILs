import sys
n,m = map(int,input().split())

arr = list(map(int,input().split()))

max_val = -sys.maxsize
ans = []

def Print():
    val = ans[0]
    if len(ans) == 1:
        return val
    else:
        for i in range(1,len(ans)):
            val ^= ans[i]
        return val


def choose(idx_num, cnt):
    global max_val

    if cnt == m:
        #print(ans , Print())
        max_val = max(max_val, Print())
        return 
    
    if idx_num == n:
        return
        
    ans.append(arr[idx_num])
    choose(idx_num+1,cnt+1)
    ans.pop()
    choose(idx_num+1,cnt)

choose(0,0)
print(max_val)