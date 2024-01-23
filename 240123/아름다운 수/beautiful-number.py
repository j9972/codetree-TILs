n = int(input())

ans = list()
res = 0

def seq():
    i = 0
    while i < n:
        if i + ans[i] - 1 >= n:
            return False

        for j in range(i,i+ans[i]):
            if ans[j] != ans[i]:
                return False
        i += ans[i]
    return True

def choose(cnt):
    global res 

    if cnt == n:
        if seq():
            res += 1
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)
print(res)