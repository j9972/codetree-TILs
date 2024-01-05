n = int(input())
arr = list(map(int,input().split()))

ans, odd, even = 0,0,0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

group = 0
while True:
    if group % 2 == 0:
        if even:
            even -= 1
            group += 1
        elif odd >= 2:
            odd -= 2
            group += 1
        else:
            if even > 0 or odd > 0:
                group -= 1
            break
    else:
        if odd:
            odd -= 1
            group += 1
        else:
            break
print(group)