n = int(input())
ans = []

def Print():
    for e in ans:
        print(e,end=' ')
    print()

visited = [False] * (n+1)

def choose(cur_idx):
    if cur_idx == n:
        Print()
        return
    
    for i in range(n,0,-1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(cur_idx + 1)

            visited[i] = False
            ans.pop()


choose(0)