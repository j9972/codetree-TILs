n = int(input())

ans = list()
res = 0

def Print():
    idx = 0

    while idx < n:
        if idx + ans[idx] - 1 >= n:
            return False
        
        for next_i in range(idx, idx + ans[idx]):
            if ans[next_i] != ans[idx]:
                return False
        
        idx += ans[idx]

    return True

def choose(cnt):
    global res

    if cnt == n:
        if Print():
            res += 1
        return 
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt + 1)
        ans.pop()

choose(0)
print(res)