n = int(input())

rsp = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


max_win = 0

win = 0
for a, b in rsp: # 1이 2를, 2가 3을 3이 1일
    if a == 1 and b == 2:
        win += 1
    elif a == 2 and b == 3:
        win += 1
    elif a == 3 and b == 1:
        win += 1

max_win = max(max_win, win)

# Case 2. 1이 3을 이기고, 3이 2를 이기고 2가 1을 이기는 경우
win = 0
for a, b in rsp: # 1이 3을 3이 2를 2가 1을
    if a == 1 and b == 3: 
        win += 1
    elif a == 3 and b == 2:
        win += 1
    elif a == 2 and b == 1:
        win += 1

max_win = max(max_win, win)

print(max_win)