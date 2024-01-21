n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
ans = []

def overapled(a,b):
    x1, y1 = a
    x2, y2 = b

    return (x1 <= x2 <= y1) or (x1 <= y2 <= y1) or (x2 <= x1 <= y2) or (x2 <= y1 <= y2)

def Possible():
    for i ,val in enumerate(ans):
        for j ,val2 in enumerate(ans):
            if i < j and overapled(val, val2):
                return False
    return True


def choose(idx, cnt):
    global max_val

    if idx == n or cnt == n:
        if Possible():
            max_val = max(max_val , len(ans))
        return 

    for i in range(cnt, n):
        ans.append(arr[i])
        choose(idx+1, cnt+1)
        ans.pop()

choose(0,0)
print(max_val)