string1 = input()
string2 = input()

dic1 = {}
dic2 = {}

for i in string1:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1        
for i in string2:
    if i in dic2:
        dic2[i] += 1
    else:
        dic2[i] = 1

if dic1==dic2:
    print('Yes')
else:
    print('No')