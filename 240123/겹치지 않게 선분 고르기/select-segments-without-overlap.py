n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = list()
max_val = 0


def possible():
    for idx1, val1 in enumerate(ans):
        for idx2, val2 in enumerate(ans):
            x1,y1 = val1
            x2,y2 = val2

            if idx1 < idx2 and ((x1<=x2<=y1) or (x1<=y2<=y1) or (x2<=x1<=y2) or (x2<=y1<=y2)):
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