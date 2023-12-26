binary = list(input())

max_cnt = 0

def cal(binary):
    sum_value = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            sum_value += 2 ** (len(binary) - i - 1)
    
    return sum_value

for i in range(len(binary)):
    if binary[i] == '1':
        binary[i] = '0'
        max_cnt = max(max_cnt, cal(binary))
        binary[i] = '1'
    else:
        binary[i] = '1'
        max_cnt = max(max_cnt, cal(binary))
        binary[i] = '0'
print(max_cnt)