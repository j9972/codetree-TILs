string = input()

cnt = 0
length = len(string)

for i in range(length):
    for j in range(i+1,length):
        if string[i] != '(':
            continue
        
        if string[j] == ')':
            cnt += 1

print(cnt)