n = int(input())

max_val = 0
ans = []

def choose(cnt):
    global max_val

    if cnt == n:
        if possible():
            max_val += 1
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

def possible():
    idx = 0

    while idx < n:

        if idx + ans[idx] - 1 >= n:
            return False
        
        for j in range(idx, idx + ans[idx]):
            if ans[idx] != ans[j]:
                return False
            
        idx += ans[idx]
    return True

choose(0)
print(max_val)