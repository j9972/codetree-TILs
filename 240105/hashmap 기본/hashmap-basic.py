n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

dic = dict()
for i in range(n):
    arr_list = arr[i]

    if arr_list[0] == 'find':
        if int(arr_list[1]) in dic:
            print(dic[int(arr_list[1])])
        else:
            print("None")
    
    else:
        if arr_list[0] == 'add':
            dic[int(arr_list[1])]  = int(arr_list[2])
        else:
            dic.pop(int(arr_list[1]))