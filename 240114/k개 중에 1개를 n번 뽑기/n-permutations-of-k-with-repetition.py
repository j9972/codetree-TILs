k,n = map(int,input().split())

ans = []
def print_answer():
    for e in ans:
        print(e, end=' ')
    print()

def choose(cur):
    if cur == n+1:
        print_answer()
        return

    for i in range(1,k+1):
        ans.append(i)
        choose(cur+1)
        ans.pop()

    return
choose(1)