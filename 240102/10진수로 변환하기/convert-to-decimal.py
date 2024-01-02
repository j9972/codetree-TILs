n = list(input())
n.reverse()

num = 0
for i in range(len(n)):
    if int(n[i]) == 1:
        num += 2 ** i
print(num)