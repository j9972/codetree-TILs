n,m = map(int,input().split())

arr = list(map(int,input().split()))

ans = []
max_val = 0
visited = [False] * (n+1)

def make_binary(val):
    binary_val = format(val,'b')
    return binary_val

def Print():
    tmp_val = ans[0]
    if len(ans) == 1:
        return tmp_val ^ tmp_val
    else:
        for i in range(1,m):
            tmp_val = tmp_val ^ ans[i]
    
        return tmp_val
    

def choose(cur):
    global max_val
    res = 0
    if cur == m:
        max_val = max(max_val, Print())
        #Print()
        return

    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            
            choose(cur+1)
            
            ans.pop()
            visited[i] = False
choose(0)
print(max_val)