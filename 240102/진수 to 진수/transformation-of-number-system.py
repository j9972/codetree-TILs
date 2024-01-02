a,b = map(int,input().split())
n = list(input())

# a -> 10 -> b

num = 0

for i in range(len(n)):
    if int(n[i]) != 0:
        num += int(n[i]) * (a**i)


def turnB(val):
    digits = []

    while True:
        if val < b:
            digits.append(val)
            break
    
        digits.append(val % b)
        val //= b
    
    result = ''
    for d in digits[::-1]:
        result += str(d)

    return result

print(turnB(num))