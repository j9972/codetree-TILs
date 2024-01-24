n = int(input())

max_val = 0
ans = list()

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def possible():

    for i,val in enumerate(ans):
        for j,val1 in enumerate(ans):
            x1,y1 = val
            x2,y2 = val1

            if i < j and ((x1 <= x2 <= y1) or (x1 <= y2 <= y1) or (x2 <= x1 <= y2) or (x2 <= y1 <= y2)):
                return False
    return True

def choose(cnt):
    global max_val

    if cnt == n:
        if possible():
            max_val = max(max_val, len(ans))
        return

    ans.append(arr[cnt])
    choose(cnt+1)
    ans.pop()
    choose(cnt+1)

choose(0)
print(max_val)