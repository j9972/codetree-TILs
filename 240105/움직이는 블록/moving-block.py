n = int(input())

block = [
    int(input())
    for _ in range(n)
]

# 결국 block의 값들의 합은 n으로 나눠지고 각각이 나눠진 값이 되야 한다
average = sum(block)//n

block.sort(reverse=True)
ans = 0

for i in range(n):
    
    if block[i] > average:
        ans += block[i] - average

print(ans)