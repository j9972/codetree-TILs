n = int(input())

ans = set()
for i in range(n):
    order, num = input().split()

    if order == 'find':
        if int(num) in ans:
            print("true")
        else:
            print("false")
    elif order == 'add':
        ans.add(int(num))
    else:
        ans.remove(int(num))