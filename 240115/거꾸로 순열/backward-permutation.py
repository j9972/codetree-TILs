n = int(input())
visited = [False] * (n+1)
ans = []
res = list()

def Print():
    string = ''
    for e in ans:
        string += str(e)
    res.append(string)

def choose(cur):
    if cur == n+1:
        Print()
        return
    
    for i in range(1,n+1):
        if visited[i]:
            continue
        
        visited[i] = True # 한번만 사용한다해서 이게 필요함
        ans.append(i)

        choose(cur+1)

        ans.pop()
        visited[i] = False
choose(1)

for i in res[::-1]:
    for j in i:
        print(j , end=' ') 
    print()