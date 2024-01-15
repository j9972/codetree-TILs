n = int(input())
visited = [False] * (n+1)
ans = []

def Print():
    for e in ans:
        print(e,end=' ')
    print()

def choose(cur):
    if cur == n+1:
        Print()
        return
    
    for i in range(1,n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        ans.append(i)

        choose(cur+1)

        ans.pop()
        visited[i] = False
choose(1)