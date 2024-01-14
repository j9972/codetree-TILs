n = int(input())

arr = list()
cnt = 0

def choose(cur):
    global cnt

    if cur == n:
        if Print():
            cnt += 1
        return

    for i in range(1,5):
        arr.append(i)
        choose(cur + 1)
        arr.pop()


def Print():
    i = 0

    while i < n:

        if i + arr[i] >= n + 1:
            return False
        
        for j in range(i, i+arr[i]):
            if arr[i] != arr[j]:
                return False

        i += arr[i]
    
    return True
choose(0)
print(cnt)