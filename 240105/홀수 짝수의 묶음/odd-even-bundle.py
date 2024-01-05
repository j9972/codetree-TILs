n = int(input())
arr = list(map(int,input().split()))

ans, odd, even = 0,0,0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    ans = odd * 2 + 1
elif even == odd:
    ans = even + odd
else:
    ans = even * 2

    size = odd - even

    if (size % 3 == 0):
        ans += (size//3) * 2
    else:
        if((size % 3) % 2 == 0):
            ans += size // 3 * 2 + 1
        else:
            ans += size // 3 * 2 - 1
print(ans)