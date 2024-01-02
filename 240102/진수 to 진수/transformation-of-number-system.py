a,b = map(int,input().split())
n = list(input())

# a -> 10 -> b

num = 0

for i in range(len(n)):
    if int(n[i]) != 0:
        num += int(n[i]) * (a**i)

digits = []

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

for d in digits[::-1]:
    print(d,end="")