a,b = map(int,input().split())
n = list(input())

# a -> 10 -> b

num = 0
for ch in n:
    num = num * a + (ord(ch) - ord('0'))

digits = []

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

for d in digits[::-1]:
    print(d,end="")