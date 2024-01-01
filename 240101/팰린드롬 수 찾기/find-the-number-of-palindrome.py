x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    string = str(i)

    if string == string[::-1]:
        ans += 1
print(ans)