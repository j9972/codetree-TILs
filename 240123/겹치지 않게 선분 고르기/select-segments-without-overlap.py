n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = list()
max_val = 0

def interact(a,b):
    x1,y1 = a
    x2,y2 = b
    return (x1 <= x2 <= y1) or (x1 <= x2 <= y1) or (x2 <= x1 <= x2) or (x2 <= y1 <= x2)

def possible():
    for i, val1 in enumerate(ans):
        for j, val2 in enumerate(ans):
            if i < j and interact(val1, val2):
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